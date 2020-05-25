import pytest

from .service import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_root_path(client):
    rv = client.get("/")
    assert rv.status == "200 OK"
    assert rv.data == b"Hello World"


def test_good_path(client):
    rv = client.get("/good")
    assert rv.status == "200 OK"
    assert rv.data == b"Good"


def test_not_found_path(client):
    rv = client.get("/bad")
    assert rv.status == "404 NOT FOUND"
