from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_Product(name, price, picture_link, description):

    Product_object = Student(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)

    session.add(Product_object)
    session.commit()


add_Product("book", 60, "https://cdn.shopify.com/s/files/1/0882/3478/articles/Book_Log_1400x.progressive.jpg?v=1549548939", "this is a cool book")

def delete_product(this.name):
	session.query().filter_by(
		name=this.name).first().delete()
	session.commit()


def update_product(name, price, picture_link, description):

	product = session.query(Product).filter_by(
		name=name).first()
	Product.name = name
	Product.picture_link = picture__link
	Product.description = description

	session.commit()

def query_all():

	Product = sesssion.query(
		Product).filter_by(
		name=this.name).first()
	return Product1

	
def add_to_cart(ProductID):

	ProductID_object=cart(
		ProductID=ProductID)
	session.add(ProductID_object)
	session.commit()


add_Product("Name", 100, "pic link", "Some Things")
products - query_all()










   


print(query_by_name("Mayuri"))
