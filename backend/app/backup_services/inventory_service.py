from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.schemas.inventory import InventorySchema, InventoryUpdateSchema

# Get inventory details by brand and product type
def get_inventory_by_brand(db: Session, brand: str = None, product_type: str = None):
    query = db.query(Inventory).join(Product)
    if brand:
        query = query.filter(Product.brand == brand)
    if product_type:
        query = query.filter(Product.product_type == product_type)
    return query.all()

# Get total stock count
def get_total_stock(db: Session):
    total_stock = db.query(Inventory).count()
    return {"total_items": total_stock}

# Update inventory
def update_inventory(db: Session, product_id: int, inventory_update: InventoryUpdateSchema):
    inventory_item = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if not inventory_item:
        return {"error": "Product not found in inventory"}
    
    inventory_item.available = inventory_update.available
    inventory_item.price = inventory_update.price
    inventory_item.quantity = inventory_update.quantity
    db.commit()
    db.refresh(inventory_item)
    return inventory_item