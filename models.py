from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    description: str | None = None
    category: str | None = None
    price: float
    stock: int
