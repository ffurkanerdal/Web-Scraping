from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///model.db")

Base = declarative_base()

class Data(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    brand = Column(String)
    price = Column(String)

Base.metadata.create_all(engine)



session = Session(bind=engine)
