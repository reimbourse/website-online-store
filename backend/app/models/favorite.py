import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base, UUIDIdMixin
from app.models.product import Product


class Favorite(Base, UUIDIdMixin):
    __tablename__ = "favorites"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"))
    added_at: Mapped[datetime] = mapped_column(server_default=func.now())

    product: Mapped["Product"] = relationship(back_populates="favorites")
