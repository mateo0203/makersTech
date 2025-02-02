from pydantic import BaseModel

# Schema for reading inventory data
class InventorySchema(BaseModel):
    product_id: int
    available: int
    price: float
    quantity: int

    class Config:
        orm_mode = True

# Schema for updating inventory
class InventoryUpdateSchema(BaseModel):
    available: int
    price: float
    quantity: int

    