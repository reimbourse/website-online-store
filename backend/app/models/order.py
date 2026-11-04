from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base, UUIDIdMixin


class Order(Base, UUIDIdMixin):
    __tablename__ = "orders"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String, default="pending")
    subtotal = Column(Numeric(10, 2))
    shipping_cost = Column(Numeric(10, 2))
    total = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("OrderItem", back_populates="order")
    shipping_address = relationship(
        "ShippingAddress", back_populates="order", uselist=False
    )


class OrderItem(Base, UUIDIdMixin):
    __tablename__ = "order_items"

    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
    variant_id = Column(UUID(as_uuid=True), ForeignKey("product_variants.id"))
    quantity = Column(Integer)
    price_at_purchase = Column(Numeric(10, 2))

    order = relationship("Order", back_populates="items")


class ShippingAddress(Base, UUIDIdMixin):
    __tablename__ = "shipping_addresses"

    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    address = Column(String)
    postal_code = Column(String)

    order = relationship("Order", back_populates="shipping_address")
