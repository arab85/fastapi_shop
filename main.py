from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from db.database import SessionLocal1,SessionLocal2,SessionLocal3,SessionLocal4,SessionLocal5, engine1 , engine2,engine3,engine4,engine5
from models import product
from models.product import text
from db.database import Base4
from crub.product import create_commodity,search_commodity,delete_commodity,create_seler,search_seler,create_text,search_text,delete_text,create_se,search_se,delete_se
from schemas.product import commodity,seller,gets,users
from sqlalchemy.orm import Session

Base4.metadata.create_all(bind=engine4)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
from api.user import router as product_router
from api.manage import router2 as product2_router
from api.seller import router3 as product3_router
from api.home_user import router4 as product4_router
app.include_router(product4_router)
app.include_router(product3_router)
app.include_router(product_router)
app.include_router(product2_router)

def get_db1():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()
def get_db4():
    db = SessionLocal4()
    try:
        yield db
    finally:
        db.close()




#صفحه اصلی
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
#صفحه کاربر
@app.get("/users", response_class=HTMLResponse)
def users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})
#صفحه ادمین
@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
#صفحه لاگ این کاربر
@app.get("/users/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
#ورود کاربر
@app.get("/users/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})
#صفحه اصلی کاربر
@app.get("/home/user", response_class=HTMLResponse)
def home_user(request: Request):
    return templates.TemplateResponse("home_user.html", {"request": request})
@app.post("/sub", response_class=HTMLResponse)
def log_admin(request: Request,
    name: str = Form(...),
    password: str = Form(...),
):
    if name == "modir" and password == "modir":
        return templates.TemplateResponse("modir.html", {"request": request , "name" : "modir"})
    if name == "admin" and password == "admin":
        return templates.TemplateResponse("modir.html", {"request": request , "name":"admin"})
    else:
        return HTMLResponse("اشتباه وارد کردی" ,status_code=401)
#صفحه اصلی ادمین
@app.get("/home/admin", response_class=HTMLResponse)
def home_user(request: Request):
    return templates.TemplateResponse("home_admin.html", {"request": request})

#مدیریت محصولات
@app.get("/home/admin/seler", response_class=HTMLResponse)
def sel(request: Request):
    return templates.TemplateResponse("seler.html", {"request": request})
#مدیریت تامین کننده ها
@app.get("/home/admin/manage", response_class=HTMLResponse)
def Manage(request: Request):
    return templates.TemplateResponse("manage.html", {"request": request})
#گزارش 
@app.get("/home/admin/report", response_class=HTMLResponse)
def report(request: Request):
    return templates.TemplateResponse("report.html", {"request": request})
@app.post("/report/sub", response_class=HTMLResponse)
def sub2(request: Request,
    subject: str = Form(...),
    tex: str = Form(...),
    db : Session = Depends(get_db4)
):
    matn = text(subject=subject , texts = tex)
    db.add(matn)
    db.commit()
    return templates.TemplateResponse("sabt9.html", {"request": request , "subject":subject})
@app.get("/home/admin/report/list", response_class=HTMLResponse)
def list(request: Request , db : Session=Depends(get_db4)):
    matns = db.query(text).all()
    return templates.TemplateResponse("list3.html", {"request": request, "matns": matns})






    