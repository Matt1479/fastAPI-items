from pydantic import BaseModel


class Item(BaseModel):
    id: int = 0
    title: str
    description: str | None = None
    category: str | None = None
    price: float = 0
    stock: int = 0
