from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.schemas.sale import SaleSchema, SaleCreateSchema
from datetime import datetime
from app.DB import hardcoded_database


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

# Get all sales data
def get_sales_data():
    """Fetch all sales data from the hardcoded database."""
    results = []
    
    for sale in hardcoded_database.hardcoded_db["sales"]:
        # Find product details
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == sale["product_id"]), None)

        # Structure the response
        results.append({
            "product_name": product["description"] if product else "Unknown Product",
            "brand": product["brand"] if product else "Unknown Brand",
            "product_type": product["product_type"] if product else "Unknown Type",
            "quantity_sold": sale["quantity"],
            "timestamp": sale["timestamp"]
        })
    
    return results
