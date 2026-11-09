import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base, UUIDIdMixin

if TYPE_CHECKING:
    from app.models.product import ProductVariant


class CartItem(Base, UUIDIdMixin):
    __tablename__ = "cart_items"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    variant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product_variants.id"))
    quantity: Mapped[int] = mapped_column(default=1)
    added_at: Mapped[datetime] = mapped_column(server_default=func.now())

    variant: Mapped["ProductVariant"] = relationship(back_populates="cart_items")
