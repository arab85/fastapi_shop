from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal1, engine1
from schemas.product import commodityBase
from models.product import commodity 
from db.database import Base1
from auth.auth import validate_number

Base1.metadata.create_all(bind=engine1)


router2 = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db1():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()

#اوایل

@router2.get("/home/admin/manage/add", response_class=HTMLResponse)
def add(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})
# حذف کالا
@router2.get("/home/admin/manage/delate", response_class=HTMLResponse)
def dalate(request: Request):
    return templates.TemplateResponse("delate.html", {"request": request})
#درخواست خرید 
@router2.get("/home/admin/manage/sel", response_class=HTMLResponse)
def sel(request: Request):
    return templates.TemplateResponse("sel.html", {"request": request})

#اضافه محصول
@router2.post("/add/sub", response_class=HTMLResponse)
def sub(
    request: Request,
    name: str = Form(...),
    sku: int = Form(...),
    price: int = Form(...),
    tedad: int = Form(...),
    min_threshold: int = Form(...),
    subject: str = Form(...),
    db: Session = Depends(get_db1)
):
    try:
        validate_number(price , tedad , sku , min_threshold)
    except HTTPException as e:
        return HTMLResponse(e.detail, status_code=e.status_code)
    kala = commodity(
        name=name,
        sku=sku,
        price=price,
        tedad=tedad,
        min_threshold=min_threshold,
        subject=subject
    )
    db.add(kala)
    db.commit()
    return templates.TemplateResponse("sabt2.html", {"request": request , "name":name ,"price":price ,"tedad": tedad})

