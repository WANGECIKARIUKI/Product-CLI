from sqlalchemy import (Column, Integer, ForeignKey, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///products.db')

Session =sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True)
    types = Column(String(), nullable=False)
    customers = relationship("Customer", backref="product")

    def __repr__(self):
        return f"{self.id} {self.types}"

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    age = Column(Integer(), nullable=False)
    email = Column(String(), nullable=False, unique=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    Review_id = Column(Integer, ForeignKey("review.id"))

    products = relationship("Product", backref="products")
    def __repr__(self):
        return f"{self.id} {self.name} {self.age} {self.email} {self.review}"
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    comment = Column(String(), nullable=False)
    customers = relationship("Customer", backref="product")



    

    def __repr__(self):
        return f"{self.id} {self.comment}"
    
Base.metadata.create_all(engine)