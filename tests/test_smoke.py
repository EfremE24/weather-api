import requests

BASE_URL = "http://localhost:8080"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

