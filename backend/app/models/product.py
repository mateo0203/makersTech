from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model_year = Column(Integer, nullable=False)
    product_description = Column(String, nullable=True)

    inventory = relationship("Inventory", back_populates="product")
    sales = relationship("Sale", back_populates="product")