from pydantic import BaseModel , Field


#کلاس کالا ها
class commodityBase(BaseModel):
    name: str = Field(min_length=1)
    sku: int 
    price: int 
    tedad: int 
    min_threshold: int 
    subject: str = Field(min_length=1)
    #pic

class commodity(commodityBase):
    id : int 
    class Config:
        orm_mode = True

#کلاس کاربران
class usersBase(BaseModel):
    fname: str = Field(min_length=1)
    lname: str = Field(min_length=1)
    kname: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)

class users(usersBase):
    id:int
    class Config:
        orm_mode = True

#کلاس تامین کننده ها
class sellerBase(BaseModel):
    name: str = Field(min_length=1)
    subject: str = Field(min_length=1, max_length=20)
    tel: int = Field(min_length=5, max_length=7)
    email : str = Field(min_length=1)
    point: int = Field(gt=1, lt=10)

class seller(sellerBase):
    id:int
    class Config:
        orm_mode = True


#کلاس گزارش ها
class textBase(BaseModel):
    subject: str = Field(min_length=1)
    text: str = Field(min_length=1)

class text(textBase):
    id:int
    class Config:
        orm_mode = True

#سفارش خرید
class getsBase(BaseModel):
    name: str = Field(min_length=1)
    tedad: int = Field(gt=0)
    subject: str = Field(min_length=1)
    name_seller : str = Field(min_length=1)
    vaziat: int = Field(gt=0, lt=4)

class gets(getsBase):
    id:int
    class Config:
        orm_mode = True


