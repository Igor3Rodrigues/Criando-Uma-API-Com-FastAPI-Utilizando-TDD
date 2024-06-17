from .database import database
from .models import ItemModel
from .schemas import ItemCreate

async def create_item(item: ItemCreate):
    item_dict = item.dict()
    result = await database["items"].insert_one(item_dict)
    item_dict["_id"] = result.inserted_id
    return ItemModel(**item_dict)

async def get_item(item_id: str):
    item = await database["items"].find_one({"_id": item_id})
    if item:
        return ItemModel(**item)
    return None
