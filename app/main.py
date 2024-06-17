from fastapi import FastAPI, HTTPException
from .schemas import ItemCreate, ItemResponse
from .crud import create_item, get_item
from pydantic import BaseModel

app = FastAPI()

@app.post("/items/", response_model=ItemResponse)
async def create_item_endpoint(item: ItemCreate):
    item = await create_item(item)
    return item

@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item_endpoint(item_id: str):
    item = await get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
