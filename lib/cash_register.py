#!/usr/bin/env python3

class CashRegister:
#Initialize the CashRegister with optional discount
  def __init__(self, discount = 0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.last_transaction = 0

  def add_item(self, title, price, quantity = 1):
       # Add item to the list and update total and last_transaction
     for i in range(quantity):
          self.items.append(title)

     self.last_transaction = price * quantity
     self.total += price * quantity

  def apply_discount(self):
      # Apply discount to the total if applicable
    if self.discount > 0:
       self.total = round(self.total - (self.total * (self.discount / 100)))
       print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
     # Remove the effect of the last transaction from the total
    self.total -= self.last_transaction