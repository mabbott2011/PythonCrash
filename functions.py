#Functions!

#Create a Functions
def sayHello():
    print('Hello')

sayHello()

#Passing parameter
def introductions(name):
    print("Hey, I'm", name)

introductions('Mikey Fitness')

#Setting a default parameter
def defaultName(defName='Rando'):
    'Print hello to name'
    print('Heya', defName)

defaultName()
#defaultName('Timmy')


# Lets pass and return some values
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,4)
print(numSum)


#Mutable and unmutable
# What can be changed and what cant once it's been created
# Strings and Integers are imutable  -> They can be over written but not changed
# Lists can be changed through a Functions

def addOneToNum(num):
    num = num + 1
    print('Value inside function', num)
    return

num = 5
addOneToNum(num)
print('Value outside function', num)

# This will alter the list perminately
def addOneToList(myList):
    myList.append(4)
    print('Value inside function', myList)
    return

myList=[1,2,3]
addOneToList(myList)
print('Value outside function', myList)
