import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/items/", json={"name": "Test Item", "description": "Test Description", "price": 10.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

@pytest.mark.asyncio
async def test_get_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/items/", json={"name": "Test Item", "description": "Test Description", "price": 10.0})
        item_id = response.json()["id"]
        response = await ac.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
