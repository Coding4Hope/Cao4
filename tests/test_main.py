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


def test_update_especies():
    payload = {
        "nome": "novo teste"
    }
    response = client.put('/especie/', json=payload)
    especie_salvo = ((response.json())["data"])[0]
    payload = {"nome" : "alterado", "especie_id": especie_salvo["especie_id"]}
    response = client.post("/especie/update/", json=payload)
    assert response.status_code == 200
    assert ((response.json())["data"][0])["nome"] == "alterado"
    assert ((response.json())["success"]) is True
    response = client.delete("/especie/delete/{0}".format(especie_salvo["especie_id"]))


def test_insert_especies():
    payload = {
        "nome": "novo teste"
    }
    response = client.put('/especie/', json=payload)
    especie_salvo = ((response.json())["data"])[0]
    assert response.status_code == 200
    assert ((response.json())["success"]) is True
    response = client.delete("/especie/delete/{0}".format(especie_salvo["especie_id"]))


def test_get_by_especies():
    payload = {
        "nome": "novo teste"
    }
    response = client.put('/especie/', json=payload)
    especie_salvo = ((response.json())["data"])[0]
    response = client.get("/especie/by-nome/{0}".format("novo"))
    assert response.status_code == 200
    assert ((response.json())["success"]) is True
    assert len((response.json())["data"]) > 0
    response = client.delete("/especie/delete/{0}".format(especie_salvo["especie_id"]))

