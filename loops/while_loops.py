#in while loops the condition is checked first. if it evaluates to true,
#  the body of the loop is executed otherwise not!

#q.)write a program to print 1 to 50 using a while loop.
i = 1
while(i<51):
    print(i)
    i = i+1

#q.) write a program to print the content of a list using while loops
l = [1,"surya",False,"this","rohan"]
i = 0
while(i<len(l)):
    print(l[i])
    i = i+1 # if ye nahi likha to infinite loops mai chala jaayega fir pura app crash hojayega 
    