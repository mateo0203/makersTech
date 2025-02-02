from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductSchema, ProductCreateSchema

# Create a new product
def create_product(db: Session, product_data: ProductCreateSchema):
    new_product = Product(**product_data.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get all products
def get_all_products(db: Session):
    return db.query(Product).all()

# Get a specific product by ID
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()

# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted"}
    return {"error": "Product not found"}
