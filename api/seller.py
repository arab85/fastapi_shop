from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal3, engine3
from schemas.product import sellerBase
from models.product import seller 
from db.database import Base3
from auth.auth import validate_number


Base3.metadata.create_all(bind=engine3)


router3 = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db3():
    db = SessionLocal3()
    try:
        yield db
    finally:
        db.close()
    

@router3.get("/home/admin/seller/add", response_class=HTMLResponse)
def add(request: Request):
    return templates.TemplateResponse("add2.html", {"request": request})

@router3.get("/home/admin/seller/delate", response_class=HTMLResponse)
def dalate(request: Request):
    return templates.TemplateResponse("delate2.html", {"request": request})

#لیست
@router3.get("/home/admin/seller/list", response_class=HTMLResponse)
def sel(request: Request ,db : Session=Depends(get_db3)):
    adams = db.query(seller).all()
    return templates.TemplateResponse("list2.html", {"request": request, "adams":adams})

#اضافه محصول
@router3.post("/add2/sub", response_class=HTMLResponse)
def sub(
    request: Request,
    name: str = Form(...),
    point: int = Form(...),
    tel : int = Form(...),
    time: int = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    db: Session = Depends(get_db3)
):
    try:
        validate_number(point , time , tel)
    except HTTPException as e:
        return HTMLResponse(e.detail, status_code=e.status_code)
    check = db.query(seller).filter(seller.name == name).first()
    if not check:

        adam = seller(
            name=name,
            point=point,
            time=time,
            email=email,
            tel=tel,
            subject=subject
        )
        db.add(adam)
        db.commit()
        return templates.TemplateResponse("sabt5.html", {"request": request , "name":name })
    else :
        return HTMLResponse("اسم تکراری است " , status_code=401)

@router3.post("/delate/sub2" , response_class=HTMLResponse)
def sub3(
    request: Request,
    name: str = Form(...),
    db: Session = Depends(get_db3)
):
    adam = db.query(seller).filter(seller.name == name).first()
    if adam is not None:
        db.query(seller).filter(seller.name == name).delete()
        db.commit()
        return templates.TemplateResponse("sabt6.html", {"request": request , "name":name} )
    else:
        return HTMLResponse("یافت نشد" , status_code=401)
