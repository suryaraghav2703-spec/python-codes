# Q.1) create a class "PROGRAMMER" for storing information of few programmers working at microsoft.
class programmer:
    company = "microsoft"
    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin 

s = programmer("surya" , 120000 , 2401045)
print(s.name , s.salary , s.pin , s.company)

k = programmer("kunal" , 110000 , 122004)
print(k.name , k.salary , k.pin ,k.company)

m = programmer("maanav" , 1000000 ,234512)
print(m.name , m.salary , m.pin , m.company)
    
# Q.2) create a class "calcultor" capable of finding square, cube , and square root of a number.
class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"square of this number is : {self.n* self.n}")

    def cube(self):
        print(f"cube of this number is : {self.n* self.n* self.n}")    

    def squareroot(self):
        print(f"square of this number is : {self.n**1/2}")    

a = calculator(int(input("enter your number:")))
a.square()
a.cube()
a.squareroot()

# Q.3) create a class with class attribute a; create an object from it and set 'a' directly using object.a = o.
#  does this change the class attribute ?
class demo:
    a = 4

o = demo()
print(o.a) # first print the class attribute because instance or object attribute is not pesent.

o.a = 0 #instance attribute is set
print(o.a) # now, instance attribute is present so it will print instance attribute.

print(demo.a) # but that doesn't mean that class atribute is changed , it will remain same but priority
# is given to instance attribute.

# Q.4) write a class train which has methods to book a ticket, get status(no. of seats)
# and get fair information of train running under indian railways.
from random import randint
class train:
    def __init__(self , trainNo):
        self.trainNO = trainNo
 
    def book(self , fro , to):
        print(f"ticket is booked in train no: {self.trainNO}from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNO} is running in time ")

    def getfare(self, fro , to):
        print(f"ticket fare in: {self.trainNO} from {fro} to {to} is {randint(222,5555)}")

t = train(123999)
t.book("rampur" , "delhi")
t.getstatus()
t.getfare("rampur" , "delhi")
    