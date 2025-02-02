from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.schemas.sale import SaleSchema, SaleCreateSchema
from datetime import datetime

# Create a new sale (purchase)
def create_sale(db: Session, sale_data: SaleCreateSchema):
    new_sale = Sale(
        product_id=sale_data.product_id,
        user_id=sale_data.user_id,
        quantity=sale_data.quantity,
        price=sale_data.price,
        timestamp=datetime.utcnow()
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale

# Get sales data for a specific product
def get_sales_data(db: Session, product_id: int = None):
    query = db.query(Sale)
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    return query.all()