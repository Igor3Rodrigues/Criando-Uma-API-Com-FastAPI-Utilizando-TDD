import pytest
from app.schemas import ItemCreate
from app.crud import create_item, get_item
from app.database import database

@pytest.mark.asyncio
async def test_create_and_get_item():
    item = ItemCreate(name="Test Item", description="Test Description", price=10.0)
    created_item = await create_item(item)
    assert created_item.name == item.name

    fetched_item = await get_item(str(created_item.id))
    assert fetched_item.name == item.name
