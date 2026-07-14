from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "Service Desk Uptime Monitor",
        "status": "running",
    }


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }


def test_check_endpoint_rejects_invalid_url() -> None:
    response = client.post(
        "/check",
        json={
            "url": "github.com",
        },
    )

    assert response.status_code == 422


def test_check_endpoint_returns_monitoring_result() -> None:
    monitoring_result = {
        "url": "https://github.com/",
        "reachable": True,
        "healthy": True,
        "status_code": 200,
        "latency_ms": 125.5,
        "error": None,
    }

    with patch(
        "app.main.check_url",
        new=AsyncMock(return_value=monitoring_result),
    ):
        response = client.post(
            "/check",
            json={
                "url": "https://github.com",
            },
        )

    assert response.status_code == 200
    assert response.json() == monitoring_result