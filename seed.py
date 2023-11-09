from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Product, Customer,Review, engine



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///products.db')
    Session = sessionmaker(bind=engine)
    session = Session()


customer = Customer(name="Lucy Kariuki", age=25, email="Lkariuki@gmail.com")
customer1 = Customer(name="Esther Muthoni", age=26, email="Emuthoni@gmail.com")
Customer2 = Customer(name="Jullian Katethya", age=27, email="Jkatethya@gmail.com")
customer3 = Customer(name="Charles Gitau", age=29, email="Cgitau@gmail.com")
customer4 = Customer(name="Alvin Njoroge", age=30, email="Anjoroge@gmail.com")
customer5 = Customer(name="Martha Wanjiku", age=32, email="Mwanjiku@gmail.com")


reviews = Review("The products provided are effective")

product = Product(type="Send Money")
product1 = Product(type="Trading")
product2 = Product(type="Loans")
product3 = Product(type="Buy Goods")
product4 = Product(type="Withdraw")

session.commit()