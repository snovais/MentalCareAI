from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_online():
    r = client.get("/")
    assert r.status_code in [200,404]

def test_diagnostico():
    r = client.post("/diagnostico", json={"sintomas": "ansiedade, insônia"})
    assert r.status_code == 200
    assert "resposta" in r.json()
