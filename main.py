from fastapi import FastAPI
from models import Item
from utils import get_items_from_api


ITEMS: list[Item] = get_items_from_api()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello, world!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in ITEMS:
        if item.id == item_id:
            return {"item": item}
    return {"error": "not found"}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"items": ITEMS[skip : skip + limit]}
