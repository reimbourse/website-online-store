import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base, UUIDIdMixin
from app.schemas.product import GenderEnum

if TYPE_CHECKING:
    from app.models.cart import CartItem
    from app.models.category import Category, Collection
    from app.models.favorite import Favorite


class Product(Base, UUIDIdMixin):
    __tablename__ = "products"

    name: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("categories.id"))
    collection_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("collections.id")
    )
    gender: Mapped[GenderEnum | None]

    category: Mapped["Category"] = relationship(back_populates="products")
    collection: Mapped["Collection"] = relationship(back_populates="products")
    variants: Mapped["ProductVariant"] = relationship(back_populates="product")
    images: Mapped["ProductImage"] = relationship(back_populates="product")
    favorites: Mapped["Favorite"] = relationship(back_populates="product")


class ProductVariant(Base, UUIDIdMixin):
    __tablename__ = "product_variants"

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"))
    color: Mapped[str]
    size: Mapped[str]
    stock: Mapped[int] = mapped_column(default=0)

    product: Mapped["Product"] = relationship(back_populates="variants")
    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="variant")


class ProductImage(Base, UUIDIdMixin):
    __tablename__ = "product_images"

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"))
    variant_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("product_variants.id")
    )

    url: Mapped[str]
    is_main: Mapped[bool] = mapped_column(default=False)

    product: Mapped["Product"] = relationship(back_populates="images")
