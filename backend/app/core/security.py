from datetime import UTC, datetime, timedelta

from argon2 import PasswordHasher, exceptions
from jose import jwt

from app.core.config import settings

PASSWORD_HASHER = PasswordHasher(time_cost=2, memory_cost=19 * 1024, parallelism=1)


def hash_password(plain_password: str) -> str:
    return PASSWORD_HASHER.hash(plain_password)


def verify_password(plain_password: str, stored_hash: str) -> bool:
    try:
        return PASSWORD_HASHER.verify(stored_hash, plain_password)
    except exceptions.VerifyMismatchError:
        return False
    except exceptions.VerificationError:
        return False


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
