#product class
class product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price=price
        self.stock=stock
        
    def __str__(self):
        return f"{self.name}-${self.price}-${self.stock}"



#customer class
class customer:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"{self.name}"

#cart item
class cartItems:
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
        

#cart
class Cart:
    def __init__(self,customer):
        self.customer=customer
        self.cart=[]
    
    def add_to_cart(self,product,quantity):
        self.cart.append(cartItems(product,quantity))
    
    def calculate_total(self):
        total_price=0
        for item in self.cart:
            total_price+=item.get_total_price()
            
        return total_price
    
    def display_cart(self):
        print(f'Sopping cart of {self.customer}')
        
        for item in self.cart:
            print(f"{item.product.name} x {item.quantity} -${item.get_total_price()}")
        
        print(f"Total: $ {self.calculate_total()}") 
        

#abstract_class
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay():
        pass

class creditcard(payment):
    def pay(self,ammount):
        print(f"paid ${ammount} using credit card")
          
        
        
        
        

laptop=product('laptop',10000,10)
phone=product('iphone',11000,20)
abdul=customer("Adbur")
abdul_cart=Cart(abdul)
abdul_cart.add_to_cart(laptop,2)
abdul_cart.add_to_cart(phone,1)

abdul_cart.display_cart()

credit_card=creditcard()
credit_card.pay(abdul_cart.calculate_total())