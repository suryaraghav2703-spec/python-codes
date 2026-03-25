# inheritance is the way of creating a new class from an existing class

class employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name is {self.name} and salary is {self.company}")

# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and salary is {self.salary}")

#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")    

                  # ye hai neeche inherited class 
class programmer(employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")    
   

a = employee()
b = programmer()
print(a.name , b.company)
            