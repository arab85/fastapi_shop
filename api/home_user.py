from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal5, engine5 , SessionLocal2 , engine2
from schemas.product import usersBase
from models.product import  users 
from db.database import Base5,Base2
from auth.auth import validate_number
from auth.auth import hash_password, verify_password, create_token ,validate_email,validate_password

Base5.metadata.create_all(bind=engine5)
Base2.metadata.create_all(bind=engine2)

 

router4 = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db5():
    db = SessionLocal5()
    try:
        yield db
    finally:
        db.close()
def get_db2():
    db = SessionLocal2()
    try:
        yield db
    finally:
        db.close()

#لیست 
@router4.get("/home/user/list", response_class=HTMLResponse)
def list(request: Request):
    return templates.TemplateResponse("list4.html", {"request": request})
#سفارش 
@router4.get("/home/user/buy", response_class=HTMLResponse)
def buy(request: Request):
    return templates.TemplateResponse("buy.html", {"request": request})
#سفارش 
@router4.get("/home/user/kif", response_class=HTMLResponse)
def kif(request: Request):
    global x
    return templates.TemplateResponse("kif.html", {"request": request  , "name" : x})

@router4.post("/vorod",response_class=HTMLResponse)
def vorod(request: Request,
          kname: str = Form(...),
          password: str = Form(...),
          db: Session = Depends(get_db2)):
    user = db.query(users).filter(users.kname == kname).first()
    if user:
        if verify_password(password, user.password):
            token = create_token({"sub": kname})
            global x
            x = kname
            return templates.TemplateResponse("vorod.html", {"request": request, "f": kname, "token": token})
        else:
            return HTMLResponse("رمز نادرست!", status_code=401)
    else:
        return HTMLResponse("کاربر یافت نشد!", status_code=401)