import pytest

from .service import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_root_path(client):
    rv = client.get("/")
    assert rv.status == "200 OK"
    assert rv.data == b'{"status": "ok"}'


def test_increment_1(client):
    rv = client.get("/add/1")
    assert rv.status == "200 OK"
    assert rv.data == b"2"


def test_increment_100(client):
    rv = client.get("/add/100")
    assert rv.status == "200 OK"
    assert rv.data == b"101"


def test_not_found_path(client):
    rv = client.get("/add/invalidString")
    assert rv.status == "404 NOT FOUND"
