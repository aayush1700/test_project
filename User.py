
class User:
  def __init__(self, firstname, lastname, username, password):
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password

  def __str__(self):
    return "Firstname = {}, Lastname = {}, username = {}".format(self.firstname, self.lastname, self.username)


class Seller(User):
  def __init__(self, firstname, lastname, username, password, usertype):
    super().__init__(firstname, lastname, username, password)
    self.usertype = usertype
    self.product_category = list()
    self.product = list()

  def __str__(self):
    return "Firstname = {}, Lastname = {}, username = {}, userType = {}".format(self.firstname, self.lastname, self.username, self.usertype)

  def add_product_category_to_seller(self, product_category, remove_or_add):
    if remove_or_add.lower() == "remove":
      self.product_category.remove(product_category)
    elif remove_or_add.lower() == "add":
      self.product_category.append(product_category)

  def add_product_to_seller(self, product, product_category):
    for category in self.product_category:
      if str(category) == product_category:
        self.product.append(product)
      else:
        print("Product category did not exists. First add product category.")

  def remove_product_to_seller(self, product, product_category):
    if product not in self.product:
      print("Product not available in catgory")
    else:
      self.product.remove(product)

class Customer(User):
  def __init__(self, firstname, lastname, username, password, usertype):
    super().__init__(firstname, lastname, username, password)
    self.usertype = usertype
    self.address = list()

  def __str__(self):
    return "Firstname = {}, Lastname = {}, username = {}, userType = {}".format(self.firstname, self.lastname, self.username, self.usertype)

  def add_user_address(self, address):
    if address not in self.address:
      self.address.append(address)
      print("User address added successfully.")
    else:
      print("User address is already present")

  def remove_user_address(self, address):
    if address in self.address:
      self.address.remove(address)
      print("User address remove successfully.")
    else:
      print("User address is not present")
