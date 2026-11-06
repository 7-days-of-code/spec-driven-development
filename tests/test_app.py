import unicodedata
from datetime import date

import app as app_module
from app import create_app


def test_empty_list(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "habitos.sqlite3")})
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Ainda não há hábitos cadastrados." in response.get_data(as_text=True)


def test_list_habits_and_duplicate_validation(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "habitos.sqlite3")})
    client = app.test_client()

    response = client.post("/habits", data={"name": "  Ler  "}, follow_redirects=True)
    assert response.status_code == 200
    assert "Ler" in response.get_data(as_text=True)
    assert "Sequência: 0" in response.get_data(as_text=True)

    response = client.post("/habits", data={"name": "   "}, follow_redirects=True)
    assert response.status_code == 200
    assert "Informe um nome para o hábito." in response.get_data(as_text=True)

    response = client.post("/habits", data={"name": "Café"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Hábito cadastrado com sucesso!" in response.get_data(as_text=True)

    duplicate_name = unicodedata.normalize("NFD", "cafe\u0301")
    response = client.post("/habits", data={"name": duplicate_name}, follow_redirects=True)
    assert response.status_code == 200
    text = response.get_data(as_text=True)
    assert "Este nome" in text
    assert "em uso" in text


def test_duplicate_name_ignores_casefold_and_unicode(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "habitos.sqlite3")})
    client = app.test_client()

    response = client.post("/habits", data={"name": "Leitura"}, follow_redirects=True)
    assert response.status_code == 200

    response = client.post("/habits", data={"name": "leitura"}, follow_redirects=True)
    assert response.status_code == 200
    text = response.get_data(as_text=True)
    assert "Este nome" in text
    assert "em uso" in text


def test_check_in_sequence_and_missing_habit(tmp_path, monkeypatch):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "habitos.sqlite3")})
    client = app.test_client()

    class FrozenDate(date):
        current = date(2026, 11, 10)

        @classmethod
        def today(cls):
            return cls.current

    monkeypatch.setattr(app_module, "date", FrozenDate)

    response = client.post("/habits", data={"name": "Leitura"}, follow_redirects=True)
    assert response.status_code == 200

    response = client.post("/habits/1/check-ins", follow_redirects=True)
    assert response.status_code == 200
    assert "Sequência: 1" in response.get_data(as_text=True)

    response = client.post("/habits/1/check-ins", follow_redirects=True)
    assert response.status_code == 200
    assert response.get_data(as_text=True).count("Sequência: 1") == 1

    FrozenDate.current = date(2026, 11, 11)
    response = client.post("/habits/1/check-ins", follow_redirects=True)
    assert response.status_code == 200
    assert "Sequência: 2" in response.get_data(as_text=True)

    FrozenDate.current = date(2026, 11, 13)
    response = client.get("/")
    assert response.status_code == 200
    assert "Sequência: 0" in response.get_data(as_text=True)

    response = client.post("/habits/1/check-ins", follow_redirects=True)
    assert response.status_code == 200
    assert "Sequência: 1" in response.get_data(as_text=True)

    response = client.post("/habits/999/check-ins")
    assert response.status_code == 404
