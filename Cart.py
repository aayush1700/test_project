class Cart:
  def __init__(self, product, quantity, customer):
    self.product = product
    self.quantity = quantity
    self.customer = customer

  def checkout_product(self):
    self.product.add_product_to_cart(self.quantity)
    print(f"Product is successfully checkout to customer name = {self.customer.username} and delivery address = {self.customer.address}")