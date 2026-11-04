from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base, UUIDIdMixin
from app.models.product import Product


class Category(Base, UUIDIdMixin):
    __tablename__ = "categories"

    name: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Collection(Base, UUIDIdMixin):
    __tablename__ = "collections"

    name: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True)
    season: Mapped[str | None]

    products: Mapped[list["Product"]] = relationship(back_populates="collection")
