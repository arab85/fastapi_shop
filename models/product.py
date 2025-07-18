from sqlalchemy import Column, Integer, String, Float
from db.database import Base1,Base2,Base3,Base4,Base5

#کالا
class commodity(Base1):
    __tablename__ = "commodites"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    sku = Column(Integer)
    price = Column(Integer)
    tedad = Column(Integer)
    min_threshold = Column(Integer)
    subject = Column(String, index=True)

#کاربران 
class users(Base2):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fname = Column(String, index=True)
    lname = Column(String, index=True)
    kname = Column(String, index=True , unique=True )
    email = Column(String, index=True , unique=True )
    password = Column(String)

#تامین کننده
class seller(Base3):
    __tablename__ = "seller"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    subject = Column(String, index=True)
    tel = Column(Integer)
    email = Column(String, index=True , unique=True)
    point = Column(Integer)
    time = Column(Integer)

#گزارش
class text(Base4):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True)
    subject = Column(String, index=True)
    texts = Column(String, index=True)

#سفارش خرید
class gets(Base5):
    __tablename__ = "list"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tedad = Column(Integer)
    subject = Column(String)
    name_seller = Column(String)
    vaziat = Column(Integer)