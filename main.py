from User import Seller, Customer
from Category_Product import Category, Product
from Cart import *

sellerList = list()
customerList = list()

def seller_menu():
  print("Welcome to E-Commerce Seller menu")

  while True:
    option = int(input("Select Option to perform the task \n"
                       "1. Add Seller if your new \n "
                       "2. Add Category. \n"
                       "3. Add Product to the Category. \n"
                       "4. Exit \n "))

    if option == 1:
      firstname = input("Enter your first name = ")
      lastname = input("Enter your last name = ")
      username = input("Enter your username = ")
      password = input("Enter your password = ")
      sellerList.append(Seller(firstname, lastname, username, password, "Seller"))
      print("Seller is successfully created")

    elif option == 2:
      username = input("Enter seller username")
      for seller in sellerList:
        if seller.username == username:
          category_type = input("Enter Category type")
          c1 = Category(category_type)
          seller.add_product_category_to_seller(c1,"add")

    elif option == 3:
      username = input("Enter seller Username.")
      for seller in sellerList:
        if seller.username == username:
          category = input("Enter Product Category")

          for cat in seller.product_category:
            if category == str(cat):
              name = input("Enter Product name")
              price = int(input("Enter Product price"))
              stock = int(input("Enter Product stock"))
              p1 = Product(name, price, stock, category)
              seller.add_product_to_seller(p1, category)
              print("Product is successfully added to seller")

    elif option == 4:
      break

def customer_menu():
  print("Welcome to E-Commerce Customer menu")

  cartMap = dict()
  while True:
    option = int(input("Select Option to perform the task \n"
                       "1. Add Customer if your new \n "
                       "2. Add Product to Cart. \n"
                       "3. Checkout the Product. \n"
                       "4. Exit \n "))

    if option == 1:
      firstname = input("Enter your first name = ")
      lastname = input("Enter your last name = ")
      username = input("Enter your username = ")
      password = input("Enter your password = ")
      customerList.append(Customer(firstname, lastname, username, password, "Customer"))
      print("Customer is successfully created")

    elif option == 2:
      c1 = None
      cust_name = input("Enter the customer name ")
      product_name = input("Enter product name= ")
      quantity = int(input("Enter quantity"))
      address = input("Enter user address")

      for cust in customerList:
        if cust.username == cust_name:
          c1 = cust
          break

      if c1 is None:
        print("Customer is not, create it first")
        break
      c1.add_user_address(address)

      seller_name = input("Enter seller name")
      for seller in sellerList:
        if seller.username == seller_name:
          for product in seller.product:
            if str(product.product_name) == product_name:
              cartMap[cust_name] = Cart(product, quantity, c1)

    elif option == 3:
      custname = input("Enter the customer name")
      print(custname)
      if custname in cartMap:
        cart = cartMap.get(custname)
        cart.checkout_product()

    elif option == 4:
      break

def main_menu():
  print("Welcome to E-Commerce store \n")

  while True:
    type_customer = input("Press 1 for seller \n Press 2 for Customer \n Press 3 for Exit \n")
    if int(type_customer) == 1:
      seller_menu()
    elif int(type_customer) == 2:
      customer_menu()
    elif int(type_customer) == 3:
      exit()

if __name__ == "__main__":
  main_menu()