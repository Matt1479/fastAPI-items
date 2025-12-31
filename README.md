# FastAPI-Items

A simple REST API written in Python and FastAPI which supports CRUD operations on items.

The API manages a collection of items stored in memory, with initial data fetched from an external API (dummyjson).

The goal of this project was to get some experience in building APIs with FastAPI, Pydantic models, and request handling.

## Setup and Run

### Clone the Repository

```bash
git clone https://github.com/Matt1479/FastAPI-Items
cd FastAPI-Items
```

### Create and Activate Virtual Environment

Refer to: https://fastapi.tiangolo.com/virtual-environments/

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
fastapi dev main.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

The docs will be available at:

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

## Endpoints

### GET /

Returns a simple welcome message.

### POST /items/

Creates an item and appends it to a list.

### GET /items/{item_id}

Returns an item with the given `item_id`.

### GET /items/

Returns a list of items.

### PUT /items/update/{item_id}

Updates an existing item.

### DELETE /items/delete/{item_id}

Deletes an item and returns it.
