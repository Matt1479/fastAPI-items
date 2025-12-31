import requests

from models import Item


def get_items_from_api(skip: int = 0, limit: int = 10) -> list[Item]:
    try:
        response_json = requests.get(
            "https://dummyjson.com/products",
            params={"skip": skip, "limit": limit}
        ).json()
    except requests.exceptions.JSONDecodeError:
        return []
    
    temp = []

    for product in response_json["products"]:
        temp.append(Item(
            id=product["id"],
            title=product["title"],
            description=product["description"],
            category=product["category"],
            price=product["price"],
            stock=product["stock"]
        ))
    
    return temp
