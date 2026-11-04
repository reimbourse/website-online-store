from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class OrderCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str
    state: str | None = None
    city: str
    address: str
    postal_code: str


class OrderResponse(BaseModel):
    id: UUID
    status: str
    subtotal: float
    shipping_cost: float
    total: float
    created_at: datetime

    class Config:
        from_attributes = True
