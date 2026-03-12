"""
Modul 1 — Projekt indítás: Health endpoint verifikáció.
Ellenőrzi, hogy a FastAPI alkalmazás fut és a /health endpoint válaszol.
"""

import importlib
import sys
from pathlib import Path


def _import_app():
    """A FastAPI app importálása a backend mappából."""
    backend_path = Path(__file__).parent.parent.parent / "backend"
    if str(backend_path) not in sys.path:
        sys.path.insert(0, str(backend_path))
    from app.main import app
    return app


def test_health_endpoint_exists():
    """A /health endpoint létezik az alkalmazásban."""
    app = _import_app()
    routes = [route.path for route in app.routes]
    assert "/health" in routes, (
        "A /health endpoint nem található. "
        "Hozd létre az app/main.py-ben: @app.get('/health')"
    )


def test_health_endpoint_returns_ok():
    """A /health endpoint 200-at ad vissza és tartalmazza a status mezőt."""
    app = _import_app()
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200, (
        f"A /health endpoint {response.status_code}-et adott vissza 200 helyett."
    )
    data = response.json()
    assert "status" in data, (
        "A /health válasz nem tartalmazza a 'status' mezőt."
    )


def test_app_title():
    """Az alkalmazásnak van title-je."""
    app = _import_app()
    assert app.title, "Az alkalmazásnak legyen title-je (FastAPI(title='...'))."
