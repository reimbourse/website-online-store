import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base, UUIDIdMixin


class Order(Base, UUIDIdMixin):
    __tablename__ = "orders"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(default="pending")
    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    shipping_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    items: Mapped[list["OrderItem"]] = relationship(back_populates="order")
    shipping_address: Mapped["ShippingAddress"] = relationship(
        back_populates="order", uselist=False
    )


class OrderItem(Base, UUIDIdMixin):
    __tablename__ = "order_items"

    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id"))
    variant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product_variants.id"))
    quantity: Mapped[int]
    price_at_purchase: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    order: Mapped["Order"] = relationship(back_populates="items")


class ShippingAddress(Base, UUIDIdMixin):
    __tablename__ = "shipping_addresses"

    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id"), unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    country: Mapped[str]
    state: Mapped[str | None]
    city: Mapped[str]
    address: Mapped[str]
    postal_code: Mapped[str]

    order: Mapped["Order"] = relationship(back_populates="shipping_address")
