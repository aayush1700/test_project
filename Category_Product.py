
class Category:
  def __init__(self, category):
    self.category = category

  def __str__(self):
    return "{}".format(self.category)

class Product():
  def __init__(self, product_name, product_price, product_stock, category):
    self.product_name = product_name
    self.product_price = product_price
    self.product_category = category
    self.product_stock = product_stock

  def __str__(self):
    return "productName = {}, ProductPrice = {}, ProductCategory = {}".format(self.product_name, self.product_price, self.product_category)

  def change_product_price(self, updated_price):
    self.product_price = updated_price

  def add_product_to_cart(self, quantity):
    if self.product_stock > 0:
      self.product_stock = self.product_stock - quantity
    else:
      print("Sufficient quantity product is not available.")