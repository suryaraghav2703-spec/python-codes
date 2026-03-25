class employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all langugages here is your language:{self.language}")


class programmer(employee , coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")    
   
a = employee()
b = programmer()

b.show()
b.printlanguages()
b.showLanguage()