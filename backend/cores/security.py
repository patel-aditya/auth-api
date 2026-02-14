from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext

from cores.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

# hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

# verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password[:72], hashed_password)

# create token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# decode token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None