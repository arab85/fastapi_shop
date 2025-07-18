from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal5, engine5
from schemas.product import getsBase
from models.product import gets 
from db.database import Base5
from auth.auth import validate_number

Base5.metadata.create_all(bind=engine5)


router2 = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db5():
    db = SessionLocal5()
    try:
        yield db
    finally:
        db.close()
