from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from models.product import users as users_model
from sqlalchemy.orm import Session
import re
from fastapi import HTTPException

SECRET_KEY = "super-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def validate_email(email: str):
    if not EMAIL_REGEX.match(email):
        raise HTTPException(status_code=400, detail="ایمیل وارد شده معتبر نیست.")

def validate_password(password: str):
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="رمز عبور باید حداقل ۸ کاراکتر باشد.")
    
def validate_number(price: int , tedad:int , sku:int , min_threshold:int):
    if price<0 or tedad<0 or sku < 0 or min_threshold<0:
        raise HTTPException(status_code=400, detail=" عدد را مثبت وارد کنید.")
