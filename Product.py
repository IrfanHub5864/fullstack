class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def getName(self):
        print(self.name)
    def getPrice(self):
        print(self.price)
prod1=Product(name="irfan",price=1000)
prod1.getName()
prod1.getPrice()