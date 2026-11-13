from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.cart import router as cart_router
from app.api.v1.favorite import router as favorite_router
from app.api.v1.order import router as order_router
from app.api.v1.product import router as product_router

base_router = APIRouter()
base_router.include_router(auth_router)
base_router.include_router(cart_router)
base_router.include_router(product_router)
base_router.include_router(order_router)
base_router.include_router(favorite_router)

v1_router = APIRouter()
v1_router.include_router(base_router, prefix="/v1")
v1_router.include_router(base_router, include_in_schema=False)
