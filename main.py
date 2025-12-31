from fastapi import FastAPI
from models import Item
from utils import get_items_from_api


ITEMS: list[Item] = get_items_from_api()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.post("/items/")
async def create_item(item: Item):
    item.id = (
        max([_item.id for _item in ITEMS if _item.id is not None]) + 1 if ITEMS else 1
    )
    ITEMS.append(item)
    return item


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in ITEMS:
        if item.id == item_id:
            return item
    return {"error": "not found"}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return ITEMS[skip : skip + limit]
