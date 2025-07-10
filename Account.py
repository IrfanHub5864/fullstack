class Account:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__balance = 0
    def getName(self):
        self.name
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance += balance
acco=Account("irfan",20)
print(acco.getBalance())
acco.setBalance(1100)
print(acco.getBalance())