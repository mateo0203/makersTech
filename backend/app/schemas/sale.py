from pydantic import BaseModel
from datetime import datetime

# Schema for reading sales data (response)
class SaleSchema(BaseModel):
    id: int
    product_id: int
    user_id: int
    quantity: int
    price: float
    timestamp: datetime

    class Config:
        orm_mode = True

# Schema for creating a new sale (request)
class SaleCreateSchema(BaseModel):
    product_id: int
    user_id: int
    quantity: int
    price: float
