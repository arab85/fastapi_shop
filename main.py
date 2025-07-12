from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from db.database import SessionLocal1,SessionLocal2,SessionLocal3,SessionLocal4,SessionLocal5, engine1 , engine2,engine3,engine4,engine5
from models import product
from crub.product import create_commodity,search_commodity,delete_commodity,create_seler,search_seler,create_text,search_text,delete_text,create_se,search_se,delete_se
from schemas.product import commodity,seller,text,gets,users
from sqlalchemy.orm import Session

product.Base1.metadata.create_all(bind=engine1)
product.Base2.metadata.create_all(bind=engine2)
product.Base3.metadata.create_all(bind=engine3)
product.Base4.metadata.create_all(bind=engine4)
product.Base5.metadata.create_all(bind=engine5)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
from api.product import router as product_router
app.include_router(product_router)

def get_db2():
    db = SessionLocal2()
    try:
        yield db
    finally:
        db.close()
def get_db3():
    db = SessionLocal3()
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
def get_db5():
    db = SessionLocal5()
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


    