from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

DATABASE_URL = settings.DATABASE_URL_pysqlite 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

def add_user(user_name: str, hashed_password: str):
    new_user = User(user_name=user_name, password = hashed_password)

    with SessionLocal() as db:
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except:
            db.rollback()
            raise ValueError("User with this name is already exists")

def get_user_by_name(user_name:str):
    with SessionLocal() as db:
        return db.query(User).filter(User.user_name == user_name).first()