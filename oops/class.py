# solving a problem by creating an object is called object oriented programming.
# a class is a blueprint for creating an object 
# class mai sirf placeholders aate hai jab class mai kuch fill kiya jata hai like class employee or anything
# tab vo ek object ban jata hai .

class employee:
    language = "py" # this is a class attribute
    salary = 120000

surya = employee()
surya.name = "surya" # this is an object/instance attribute
print(surya.name , surya.salary , surya.language)

kunal = employee()
kunal.name = "kunal kashayp"
print(kunal.name , kunal.salary , kunal.language)

# Here name is object attribute and salary and language are class
# attributes as they directly belong to the class.



            #   INSTANCE VS CLASS ATTRIBUTE

class employee:
    language = "py" # this is a class attribute
    salary = 1234567

harry = employee()
harry.language = "javaScript" # this is an instance attribute
print(harry.language , harry.salary)
   
# Instance  attribute take priferrence over class attribute upar class mai python tha 
# but instance mai java script to java script ko preferrence di jayegi.



            # SELF PARAMETER
# self refers to he instance of the class. it is automatically passed with a function call from an object.

class employee:
    language = "python"
    salary = 130000

    def getInfo(self):
        print(f"your language is {self.language}. and\n  salary is {self.salary}") 

    def greet(self):
        print("Good Morning")

m = employee()
m.greet()
m.getInfo() 

                         #    STATIC METHOD
# sometimes we need a function that does not use the self-parameter. we can define a static method like this:
@staticmethod  # decorater to mark as a static method
def greet():
    print("hello user")     


                        #  __init__() constructor
# __init__() is the special method which is first run as soon as the object is created.
# it takes self arguments and can also take further arguments
class Employee:
    def __init__(self , name , salary , language):  # it is a dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

harry = Employee("harry" , 1300000 , "javScript")   
print(harry.name , harry.salary , harry.language)     

        