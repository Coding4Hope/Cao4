from fastapi.testclient import TestClient
from starlette import responses
# from models import especie
from main import app

import requests


client = TestClient(app)


def test_get_especies():
    response = client.get("/especie")
    assert response.status_code == 200
    assert ((response.json())["success"]) is True


def test_delete_especies():
    payload = {
        "nome": "novo teste"
    }
    response = client.put('/especie/', json=payload)
    especie_salvo = ((response.json())["data"])[0]
    response = client.delete("/especie/delete/{0}".format(especie_salvo["especie_id"]))
    assert response.status_code == 200
    assert ((response.json())["success"]) is True
