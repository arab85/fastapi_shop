from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal1, engine1 , SessionLocal2 , engine2
from schemas.product import usersBase
from models.product import  users , commodity
from db.database import Base1,Base2
from auth.auth import validate_number
from auth.auth import hash_password, verify_password, create_token ,validate_email,validate_password

Base1.metadata.create_all(bind=engine1)
Base2.metadata.create_all(bind=engine2)

x = None
a = []

router4 = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db1():
    db = SessionLocal1()
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
def list1(request: Request):
    return templates.TemplateResponse("list4.html", {"request": request})
#لیست 
@router4.get("/home/user/list1", response_class=HTMLResponse)
def list2(request: Request , db: Session = Depends(get_db1)):
    kalas = db.query(commodity).order_by(commodity.price.asc()).all()
    return templates.TemplateResponse("list5.html", {"request": request , "k":kalas})
@router4.post("/buy/sab2", response_class=HTMLResponse)
async def b(request: Request):
    form_data = await request.form()
    global a
    a = form_data.getlist("selected")
    return templates.TemplateResponse("sabt11.html", {"request": request})

#لیست 
@router4.get("/home/user/list2", response_class=HTMLResponse)
def list3(request: Request, db: Session = Depends(get_db1), subject: str = None):
    subjects = db.query(commodity.subject).distinct().all()
    subjects = [s[0] for s in subjects]

    kalas = []
    if subject:
        kalas = db.query(commodity).filter(commodity.subject == subject).order_by(commodity.name.asc()).all()
    
    return templates.TemplateResponse("list6.html", {
        "request": request,
        "subjects": subjects,
        "selected_subject": subject,
        "k": kalas
    })

#لیست 
@router4.get("/home/user/list3", response_class=HTMLResponse)
def list4(request: Request , db: Session = Depends(get_db1)):
    kalas = db.query(commodity).order_by(commodity.name.asc()).all()
    return templates.TemplateResponse("list5.html", {"request": request , "k":kalas})
#سفارش 
@router4.get("/home/user/buy", response_class=HTMLResponse)
def buy(request: Request , db : Session=Depends(get_db1) , db2 : Session = Depends(get_db2)):
    q = 0
    global a,x
    user = db2.query(users).filter(users.kname == x).first()
    if user is None:
        return HTMLResponse("وارد شوید", status_code=401)
    else:
        b = user.kifp

    for i in range (len(a)):
        q +=db.query(commodity).filter(commodity.id==a[i]).first().price
        c = a[i]
        a[i] = db.query(commodity).filter(commodity.id==a[i]).first().name
    if q<= b and db.query(commodity).filter(commodity.id==c).first().tedad>0 :
        b-=q
        db.query(commodity).filter(commodity.id==c).first().tedad -= 1   
        db.commit()
        db2.commit()
        return templates.TemplateResponse("buy.html", {"request": request , "a":a, "b":b})
    else:
        return HTMLResponse("موجودی کم ", status_code=401)
#سفارش 
@router4.get("/home/user/kif", response_class=HTMLResponse)
def kif(request: Request,db: Session = Depends(get_db2)):
    global x
    if x is not None:
        name = db.query(users).filter(users.kname == x).first()
        return templates.TemplateResponse("kif.html", {"request": request  , "name" : name.kname , "pol" : name.kifp})
    else:
        return HTMLResponse("  دوباره ورود کنید /nکاربر یافت نشد!", status_code=401)

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

@router4.post("/sharg",response_class=HTMLResponse)
def sha(request: Request,
          kname: str = Form(...),
          toman: int = Form(...),
          db: Session = Depends(get_db2)):
    user = db.query(users).filter(users.kname == kname).first()
    if user:
        user.kifp+=toman
        db.commit()
        return HTMLResponse("کاربر یافت شد!", status_code=200)

    else:
        return HTMLResponse("کاربر یافت نشد!", status_code=401)