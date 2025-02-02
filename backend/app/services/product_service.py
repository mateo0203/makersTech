from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductSchema, ProductCreateSchema
from app.DB import hardcoded_database


# Create a new product
def create_product(db: Session, product_data: ProductCreateSchema):
    new_product = Product(**product_data.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get all products
def get_all_products():
    """Fetch all products along with their inventory details from the hardcoded database."""
    results = []
    
    for product in hardcoded_database.hardcoded_db["products"]:
        # Find the corresponding inventory data
        inventory_item = next((item for item in hardcoded_database.hardcoded_db["inventory"] if item["product_id"] == product["product_id"]), None)

        # Structure the response
        results.append({
            "product_id": product["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "product_description": product.get("description", "No description available"),
            "available": inventory_item["available"] if inventory_item else False,
            "price": inventory_item["price"] if inventory_item else None,
            "quantity": inventory_item["quantity"] if inventory_item else 0
        })
    
    return results

def not_related_to_ecommerce_data():
    return "La IA esta para responder preguntas relacionadas al Ecommerce de makers. Cuando preguntan algo no relacionado con makers o tratan de hacer conversación, solo responda amablemente."



# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted"}
    return {"error": "Product not found"}
