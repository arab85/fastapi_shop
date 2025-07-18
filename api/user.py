from fastapi import APIRouter, Request, Form, Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.database import SessionLocal2, engine2
from schemas.product import usersBase
from models.product import users as users_model
from auth.auth import hash_password, verify_password, create_token ,validate_email,validate_password
from db.database import Base2

Base2.metadata.create_all(bind=engine2)


router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_db2():
    db = SessionLocal2()
    try:
        yield db
    finally:
        db.close()

#ثبت نام
@router.post("/sabt", response_class=HTMLResponse)
def register(
    request: Request,
    fname: str = Form(...),
    lname: str = Form(...),
    kname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db2)
):
    try:
        validate_email(email)
        validate_password(password)
    except HTTPException as e:
        return HTMLResponse(e.detail, status_code=e.status_code)

    user = db.query(users_model).filter(users_model.kname == kname).first()
    em = db.query(users_model).filter(users_model.email == email).first()

    if user:
        return HTMLResponse("نام کاربری تکراری است", status_code=401)
    if em:
        return HTMLResponse("ایمیل تکراری است", status_code=401)
    # چک رمز تکراری هم در صورت نیاز می‌تونی اضافه کنی

    hashed = hash_password(password)
    new_user = users_model(
        kifp = 0,
        fname=fname,
        lname=lname,
        kname=kname,
        email=email,
        password=hashed
    )
    db.add(new_user)
    db.commit()
    token = create_token({"sub": kname, "nam": fname, "nam2": lname})
    return templates.TemplateResponse("sabt.html", {"request": request, "username": fname, "username2": lname, "token": token})


