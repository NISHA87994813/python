from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str  # Required field
    description: Optional[str] = None  # Optional field (no required symbol)
    price: float  # Required field
    tax: Optional[float] = None  # Optional field (no required symbol)

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
