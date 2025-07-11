from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#کالا های فروشگاه
SQLALCHEMY_DATABASE_URL1 = "sqlite:///./commodity.db"

engine1 = create_engine(
    SQLALCHEMY_DATABASE_URL1,
    connect_args={"check_same_thread": False}
)

SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine1)
Base1 = declarative_base()

#کاربران فروشگاه
SQLALCHEMY_DATABASE_URL2 = "sqlite:///./users.db"

engine2 = create_engine(
    SQLALCHEMY_DATABASE_URL2,
    connect_args={"check_same_thread": False}
)

SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)
Base2 = declarative_base()

#تامین کننده های فروشگاه
SQLALCHEMY_DATABASE_URL3 = "sqlite:///./commodity.db"

engine3 = create_engine(
    SQLALCHEMY_DATABASE_URL3,
    connect_args={"check_same_thread": False}
)

SessionLocal3 = sessionmaker(autocommit=False, autoflush=False, bind=engine3)
Base3 = declarative_base()

#گزارش ها
SQLALCHEMY_DATABASE_URL4 = "sqlite:///./commodity.db"

engine4 = create_engine(
    SQLALCHEMY_DATABASE_URL4,
    connect_args={"check_same_thread": False}
)

SessionLocal4 = sessionmaker(autocommit=False, autoflush=False, bind=engine4)

Base4 = declarative_base()