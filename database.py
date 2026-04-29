from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

D_url="sqlite:///./kuppam.db"

engine = create_engine(
    D_url,
    connect_args={"check_same_thread": False}
  
)

SessionLocal =sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    