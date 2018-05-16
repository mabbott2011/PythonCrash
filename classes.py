# Classes & Objects

class Person:
    __name = ''
    __email = ''

    # the constructor
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)

class Customer(Person):
    """docstring for Customer."""
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name,email)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self,email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def getDebtInfo(self):
        return '{} owes {} and can be contacted at {} for payment'.format(self.__name,self.__balance,self.__email)

# Time to get out of the class and start making People
"""
brad = Person()
brad.set_name('Brad Traversy')
brad.set_email('brad@gmail.com')


print(brad.get_name())
print(brad.get_email())
"""

tony = Person('Tony Romero', 'TonyRomero@gmail.com')
print('Name:',tony.get_name())
print('Email:',tony.get_email())

print(tony.toString())


John = Customer('John Doe','John.Doe@gmail.com',100)
print(John.getDebtInfo())
John.setBalance(300)
print(John.getDebtInfo())
