#!/usr/bin/env python3

# import ipdb 

class CashRegister:
    
    def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      print(f"This is the starting total: {self.total}.")

    def add_item(self, title, price=0, quantity=1):
      new_total = price * quantity
      self.last_transaction = new_total
      for item in range(quantity):
        self.items.append(title)
      self.total = self.total + new_total
      print(f"This is the total before discounts: ${self.total}.")

    def apply_discount(self):
      if (self.discount > 0):
        discount_percent = self.discount / 100
        money_off = self.total * discount_percent
        self.total = int(self.total - money_off)
        print(f"After the discount, the total comes to ${self.total}.")
      else:
        print("There is no discount to apply.")
    
    def void_last_transaction(self):
      self.total = self.total - self.last_transaction
      print(f"After voiding the last transaction, the total comes to ${self.total}.")
    

register1 = CashRegister(10)
register1.add_item("bread", 100, 1)
register1.add_item("cereal", 100, 2)
register1.apply_discount()
register1.void_last_transaction()
