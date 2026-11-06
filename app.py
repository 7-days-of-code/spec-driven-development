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


def normalize_habit_name(value):
    if value is None:
        return ""
    return unicodedata.normalize("NFC", value.strip())


def get_habit_sequence(db, habit_id, today=None):
    if today is None:
        today = date.today()

    rows = db.execute(
        "SELECT completed_on FROM habit_checkin WHERE habit_id = ? ORDER BY completed_on DESC",
        (habit_id,),
    ).fetchall()

    if not rows:
        return 0

    last_date = date.fromisoformat(rows[0]["completed_on"])
    if last_date < today - timedelta(days=1):
        return 0

    streak = 0
    cursor = last_date
    while True:
        existing = db.execute(
            "SELECT 1 FROM habit_checkin WHERE habit_id = ? AND completed_on = ?",
            (habit_id, cursor.isoformat()),
        ).fetchone()
        if existing is None:
            break
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
        habits = db.execute("SELECT id, name FROM habit ORDER BY id").fetchall()
        today = date.today()
        habit_rows = []
        for habit in habits:
            habit_rows.append(
                {
                    "id": habit["id"],
                    "name": habit["name"],
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
