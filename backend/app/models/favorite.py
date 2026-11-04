from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base, UUIDIdMixin


class Favorite(Base, UUIDIdMixin):
    __tablename__ = "favorites"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    added_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", foreign_keys=[product_id])
