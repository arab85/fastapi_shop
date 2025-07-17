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
#ادیت
@router2.get("/home/admin/manage/edit", response_class=HTMLResponse)
def edit2(request: Request):
    return templates.TemplateResponse("edit2.html", {"request": request})


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
    check = db.query(commodity).filter(commodity.sku == sku).first()
    if not check:

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
    else :
        return HTMLResponse("sku تکراری است " , status_code=401)

@router2.post("/delate/sub" , response_class=HTMLResponse)
def sub(
    request: Request,
    sku: int = Form(...),
    db: Session = Depends(get_db1)
):
    kala = db.query(commodity).filter(commodity.sku == sku).first()
    if kala is not None:
        name = db.query(commodity).filter(commodity.sku == sku).first().name
        db.query(commodity).filter(commodity.sku == sku).delete()
        db.commit()
        return templates.TemplateResponse("sabt3.html", {"request": request , "name":name} )
    else:
        return HTMLResponse("یافت نشد" , status_code=401)
    


#خرید با نقطه خرید
@router2.get("/min_threshold")
def show_min_threshold(request: Request, db: Session = Depends(get_db1)):
    kalas = db.query(commodity).filter(commodity.min_threshold == commodity.tedad).all()
    return templates.TemplateResponse("min_threshold.html", {"request": request, "kalas": kalas})


#خرید فرمی
@router2.post("/buy/sub" , response_class=HTMLResponse)
def buy(
    request: Request,
    sku: int = Form(...),
    tedad: int = Form(...),
    db: Session = Depends(get_db1)
):
    kala = db.query(commodity).filter(commodity.sku == sku).first()
    
    if kala is not None:
        name = kala.name
        kala . tedad = kala.tedad + tedad
        db.commit()
        return templates.TemplateResponse("sabt4.html", {"request": request , "name" : name} )
    else:
        return HTMLResponse("یافت نشد" , status_code=401)
    
#لیست
@router2.get("/home/admin/commodity", response_class=HTMLResponse)
def list(request: Request , db: Session = Depends(get_db1)):
    kalas = db.query(commodity).all()
    return templates.TemplateResponse("list1.html", {"request": request, "kalas": kalas})

#ویاریش
@router2.post("/edit/sub2", response_class=HTMLResponse)
def edit(
    request: Request,
    name: str = Form(""),
    price: int = Form(0),
    sku : int = Form(0),
    min_threshold: int = Form(0),
    subject: str = Form(""),
    namea: str = Form(...),
    db: Session = Depends(get_db1)
):
    try:
        validate_number(price , sku , min_threshold)
    except HTTPException as e:
        return HTMLResponse(e.detail, status_code=e.status_code)
    check = db.query(commodity).filter(commodity.name == namea).first()
    if check:
        if name != "":
            check.name=name
        if price !=0:
            check.price=price
        if sku !=0:
            check.sku=sku
        if min_threshold !=0:
            check.min_threshold=min_threshold
        if subject != "":
            check.subject=subject

        

        db.commit()
        return templates.TemplateResponse("sabt8.html", {"request": request , "name":namea })
    else :
        return HTMLResponse("اسم  نیست " , status_code=401)