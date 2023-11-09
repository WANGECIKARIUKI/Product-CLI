from models import Product, Customer,Review, engine, session


customers = Customer
reviews = Review
products = Product
user_session = {}

def add_customers():
    session.query(Product).delete()
    session.commit()
    for i in products:
        comments = Product(customer = i, comment = reviews)
        session.add(comments)
        session.commit()


def read_comments():
    reviews = input("Please choose a review: ")
    customers = int(input("and comment: "))


def user_registration():
    user = add_customers(username = input("Your name please: "),
                 email = input("Email: "))
    session.add(customers)
    session.commit()

    print(f"Welcome ! {customers.username} \n")
    
def return_user():
    user_login = input("Please enter your email to sign in: ")
    result = session.query(Customer).filter(Customer.email == user_login).first()

    print(f"Welcome back ! {result.username}")

def make_reviews():
    result = session.query(Product).filter(Product.reviews == user_session[""]).first()

    new_review = reviews(title = str(input("Please write your review: ")),
                        comment = str(input("Start writing comments here : ")),
                        customer_id = user_session['user_logged'].id,
                        bible_id = result.id)
    session.add(reviews)
    session.commit()

    

def app():
    
    choice = 0 

    while choice != 3:
        print("\n *** Welcome to Lucash App *** \n")
        print(" 1. Choose a product ")
        print(" 2. Leave a review ")
        print(" 3. Exit \n")
        choice = int(input())
        

        if choice == 1:
            ans = input("Are you new? y/n: ")

            if ans == 'y':
                user_registration()
                Product.select()
                make_reviews()

            else:
                return_user()
                Product.select()
                make_reviews()
            
        elif choice == 2:
            ans = input("Are you new? y/n: ")
            
            if ans == 'y':
                user_registration()

                print("Creating an account ...")
                

                Product.select()
                make_reviews()

            else:
                return_user()

                Product.select()
                make_reviews()

            choice = 3




if __name__ == '__main__':
    
    app()



    #from sqlalchemy.orm import sessionmaker
#from models import Product, Customer,Review, engine

#Session = sessionmaker(bind=engine)
#session = Session()
#customers = session.query(Customer).all()

#reviews = session.query(Review).all()

#products = session.query(Product).all()
#customer = Customer[0]
#print (customer.id, customer.name, customer.age)
#print (reviews)
#print (products)

#customer = Customer(name="Lucy Kariuki", age=25, email="Lkariuki@gmail.com")
#customer1 = Customer(name="Esther Muthoni", age=26, email="Emuthoni@gmail.com")
#customer2 = Customer(name="Jullian Katethya", age=27, email="Jkatethya@gmail.com")
#customer3 = Customer(name="Charles Gitau", age=29, email="Cgitau@gmail.com")
#customer4 = Customer(name="Alvin Njoroge", age=30, email="Anjoroge@gmail.com")
#customer5 = Customer(name="Martha Wanjiku", age=32, email="Mwanjiku@gmail.com")


#reviews = Review("The products provided are effective")

#product = Product(type="Send Money")
#product1 = Product(type="Trading")
#product2 = Product(type="Loans")
#product3 = Product(type="Buy Goods")
#product4 = Product(type="Withdraw")