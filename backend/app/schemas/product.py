from pydantic import BaseModel
from typing import Optional

# Schema for reading product data (response)
class ProductSchema(BaseModel):
    product_id: int
    product_type: str
    brand: str
    product_description: Optional[str] = None

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models

# Schema for creating a new product (request)
class ProductCreateSchema(BaseModel):
    product_type: str
    brand: str
    product_description: Optional[str] = None
