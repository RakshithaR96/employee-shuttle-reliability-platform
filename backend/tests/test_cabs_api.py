import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client


def test_create_cab(client: TestClient) -> None:
    response = client.post(
        "/api/cabs",
        json={
            "registration_number": "KA01AB1234",
            "display_name": "Metro Shuttle 1",
            "capacity": 12,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] > 0
    assert data["registration_number"] == "KA01AB1234"
    assert data["display_name"] == "Metro Shuttle 1"
    assert data["capacity"] == 12
    assert data["is_active"] is True


def test_duplicate_registration_number(client: TestClient) -> None:
    payload = {
        "registration_number": "KA02CD5678",
        "display_name": "Metro Shuttle 2",
        "capacity": 10,
    }

    first_response = client.post(
        "/api/cabs",
        json=payload,
    )

    second_response = client.post(
        "/api/cabs",
        json=payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409


def test_list_cabs(client: TestClient) -> None:
    response = client.get("/api/cabs")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_cab(client: TestClient) -> None:
    create_response = client.post(
        "/api/cabs",
        json={
            "registration_number": "KA03EF9012",
            "display_name": "Metro Shuttle 3",
            "capacity": 8,
        },
    )

    assert create_response.status_code == 201

    cab_id = create_response.json()["id"]

    response = client.get(f"/api/cabs/{cab_id}")

    assert response.status_code == 200
    assert response.json()["id"] == cab_id


def test_get_missing_cab(client: TestClient) -> None:
    response = client.get("/api/cabs/999999")

    assert response.status_code == 404