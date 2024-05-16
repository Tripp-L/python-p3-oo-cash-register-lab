#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0): # __init__ initializes attributes of a new 'CashRegister' object
  # 'discount=0' means ifno discount is given , it defaults to 0.
    self.discount = discount #initialized 'discount' attribute
    self.total = 0 #initializes 'total' attribute to 0, and keeps track of total amount.
    self.items = [] #initializes 'items' attribute as an empty list, which stores the titles of purchased items.
    self.last_item_price = 0 #initializes 'last_item_price' attribute to 0, and stores price of last item added.
    self.last_item_quantity = 0 #initializes 'last_item_quantity' attribute to 0, and stores the quantity of last item added.
    
  def add_item(self, title, price, quantity=1): # 'add_item' adds an item to the cash register.
    # 'title'=> name of item, 'price'=> price of item, 'quantity=1'=> number of items added, and defaults to 1 if not secified.
    self.total += price * quantity #increases 'total' by price of the added items.
    self.items.extend([title] * quantity) # adds item title to 'items' list, repeats 'quantity' times.
    self.last_item_price = price # updates 'last_item_price' with price of added item
    self.last_item_quantity = quantity # updates 'last_item_quantity' with the quantity of added item.
    
  def apply_discount(self): 
    if self.discount > 0:  #checks if 'discount' is greater than 0.
      discount_amount = self.total * (self.discount / 100) #calculates discount amount.
      self.total -= discount_amount #reduces 'total' by discount amount.
      print("After the discount, the total comes to $800.") # message to indicate new total after discount.
    else:
      print("There is no discount to apply.") #message to indicate no discount if discount not applied.
      
  def void_last_transaction(self): # removes last items added from cash register.
    if self.last_item_quantity > 0: #checks if las item's quantity is greater than 0.
      self.total -= self.last_item_price * self.last_item_quantity #decreases 'total' by price of last items added multiplied by their quantity.
      self.items = self.items[:len(self.items) - self.last_item_quantity] # removes last 'last_item_quantity' items from 'items' list.
      self.last_item_price = 0 #resets 'last_item_price' to 0.
      self.last_item_quantity = 0 # resets 'last_item_quantity' to 0.
      
      
      
    
      
      
  
