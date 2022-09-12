from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_resource():
    response_auth = client.get("/")
    assert response_auth.status_code == 200


def test_child_resource():
    response_auth = client.get("/gql")
    assert response_auth.status_code == 200
