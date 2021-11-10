from fastapi.testclient import TestClient
import requests
from starlette import responses

from main import app
from models import especie

client = TestClient(app)


def test_get_especies():
    response = client.get("/especie")
    assert response.status_code == 200
    assert ((response.json())["success"]) is True


def test_delete_especies():
    response = client.delete("/delete/{especie_id}")
    assert response.status_code == 200
    assert ((response.json())["success"]) is True