from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    available = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="inventory")