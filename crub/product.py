from sqlalchemy.orm import Session
from models.product import commodity
from schemas.product import commodityBase
from models.product import users
from schemas.product import usersBase
from models.product import seller
from schemas.product import sellerBase
from models.product import text
from schemas.product import textBase
from models.product import gets
from schemas.product import getsBase

#کراب کالا ها
def create_commodity(db: Session, jens: commodityBase):
    db_product = commodity(**jens.dict())
    db.add(db_product)
    db.commit()

def search_commodity(db: Session, n : str = "", sku : int = 0):

    kala = db.query(commodity).filter(commodity.sku == sku).first()
    if kala is not None:
        return f"{kala.name}         {kala.price}         {kala.tedad}       {kala.sku}"
    else:
        kala = db.query(commodity).filter(commodity.name == n).first()
        if kala is not None:
            return f"{kala.name}         {kala.price}         {kala.tedad}       {kala.sku}"
        else:
            return "no"#main
        
def delete_commodity(db: Session, n : str = "", sku : int = 0):
    db.query(commodity).filter(commodity.name == n).delete()
    db.query(commodity).filter(commodity.sku == sku).delete()
    db.commit()     


#کراب تامین کننده
def create_seler(db: Session, adam: sellerBase):
    seller = seller(**adam.dict())
    db.add(seller)
    db.commit() 

def search_seler(db: Session, n : str = ""):

    adam = db.query(seller).filter(seller.name == n).first()
    if adam is not None:
        return f"{adam.name}"
    else:
        return "no"#main
    
#گزارش
def create_text(db: Session, matn: textBase):
    db_product = text(**matn.dict())
    db.add(db_product)
    db.commit()

def search_text(db: Session, n : str = ""):

    goza = db.query(seller).filter(seller.name == n).first()
    if goza is not None:
        return f"{goza.name}"
    else:
        return "no"#main
        
def delete_text(db: Session, n : str = ""):
    db.query(text).filter(text.name == n).delete()
    db.commit() 

#سفارش
def create_se(db: Session, matn: getsBase):
    db_product = gets(**matn.dict())
    db.add(db_product)
    db.commit()

def search_se(db: Session, n : str = ""):

    sel = db.query(gets).filter(gets.name == n).first()
    if sel is not None:
        return f"{sel.name}"
    else:
        return "no"#main
        
def delete_se(db: Session, n : str = ""):
    db.query(gets).filter(gets.name == n).delete()
    db.commit()