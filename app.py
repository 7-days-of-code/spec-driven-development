import os
import sqlite3
import unicodedata
from datetime import date, timedelta

from flask import Flask, current_app, flash, g, redirect, render_template, request, url_for


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as schema_file:
        db.executescript(schema_file.read().decode("utf-8"))
    columns = {row["name"] for row in db.execute("PRAGMA table_info(habit)")}
    if "weekly_goal" not in columns:
        db.execute(
            "ALTER TABLE habit ADD COLUMN weekly_goal INTEGER "
            "CHECK (weekly_goal IS NULL OR weekly_goal BETWEEN 1 AND 7)"
        )
        db.commit()


def normalize_habit_name(value):
    if value is None:
        return ""
    return unicodedata.normalize("NFC", value.strip())


def get_habit_sequence(db, habit_id, today=None):
    if today is None:
        today = date.today()

    checkin_dates = {
        date.fromisoformat(row["completed_on"])
        for row in db.execute(
            "SELECT completed_on FROM habit_checkin WHERE habit_id = ?",
            (habit_id,),
        ).fetchall()
    }

    if not checkin_dates:
        return 0

    last_date = max(checkin_dates)
    if last_date < today - timedelta(days=1):
        return 0

    streak = 0
    cursor = last_date
    while cursor in checkin_dates:
        streak += 1
        cursor -= timedelta(days=1)

    return streak


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "habitos.sqlite3"),
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
    app.teardown_appcontext(close_db)

    @app.route("/", methods=["GET"])
    def index():
        db = get_db()
        habits = db.execute(
            "SELECT id, name, weekly_goal FROM habit ORDER BY id"
        ).fetchall()
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        habit_rows = []
        for habit in habits:
            weekly_progress = None
            weekly_goal_met = False
            if habit["weekly_goal"] is not None:
                progress = db.execute(
                    "SELECT COUNT(DISTINCT completed_on) AS days_marked "
                    "FROM habit_checkin "
                    "WHERE habit_id = ? AND completed_on BETWEEN ? AND ?",
                    (habit["id"], week_start.isoformat(), week_end.isoformat()),
                ).fetchone()
                weekly_progress = progress["days_marked"]
                weekly_goal_met = weekly_progress >= habit["weekly_goal"]

            habit_rows.append(
                {
                    "id": habit["id"],
                    "name": habit["name"],
                    "weekly_goal": habit["weekly_goal"],
                    "weekly_progress": weekly_progress,
                    "weekly_goal_met": weekly_goal_met,
                    "sequence": get_habit_sequence(db, habit["id"], today),
                }
            )
        return render_template("index.html", habits=habit_rows)

    @app.route("/habits", methods=["POST"])
    def create_habit():
        raw_name = request.form.get("name", "")
        name = normalize_habit_name(raw_name)

        if not name:
            flash("Informe um nome para o hábito.", "error")
            return redirect(url_for("index"))

        name_key = unicodedata.normalize("NFC", name).casefold()
        db = get_db()

        try:
            db.execute(
                "INSERT INTO habit (name, name_key) VALUES (?, ?)",
                (name, name_key),
            )
            db.commit()
            flash("Hábito cadastrado com sucesso!", "success")
        except sqlite3.IntegrityError:
            flash("Este nome já está em uso.", "error")

        return redirect(url_for("index"))

    @app.route("/habits/<int:habit_id>/weekly-goal", methods=["POST"])
    def set_weekly_goal(habit_id):
        db = get_db()
        habit = db.execute("SELECT id FROM habit WHERE id = ?", (habit_id,)).fetchone()
        if habit is None:
            return ("", 404)

        raw_days = request.form.get("days")
        if raw_days is None:
            flash("Informe uma meta de 1 a 7 dias por semana.", "error")
            return redirect(url_for("index"))

        days = raw_days.strip()
        if not days:
            db.execute("UPDATE habit SET weekly_goal = NULL WHERE id = ?", (habit_id,))
            db.commit()
            flash("Meta semanal removida.", "success")
            return redirect(url_for("index"))

        try:
            weekly_goal = int(days)
        except ValueError:
            weekly_goal = None

        if weekly_goal is None or not 1 <= weekly_goal <= 7:
            flash("Informe uma meta de 1 a 7 dias por semana.", "error")
            return redirect(url_for("index"))

        db.execute(
            "UPDATE habit SET weekly_goal = ? WHERE id = ?",
            (weekly_goal, habit_id),
        )
        db.commit()
        flash("Meta semanal atualizada.", "success")
        return redirect(url_for("index"))

    @app.route("/habits/<int:habit_id>/check-ins", methods=["POST"])
    def check_in_habit(habit_id):
        db = get_db()
        habit = db.execute("SELECT id FROM habit WHERE id = ?", (habit_id,)).fetchone()
        if habit is None:
            return ("", 404)

        today = date.today().isoformat()
        try:
            db.execute(
                "INSERT INTO habit_checkin (habit_id, completed_on) VALUES (?, ?)",
                (habit_id, today),
            )
            db.commit()
        except sqlite3.IntegrityError:
            db.rollback()

        return redirect(url_for("index"))

    with app.app_context():
        init_db()

    return app
