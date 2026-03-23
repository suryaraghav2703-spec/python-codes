# Write a program using functions to find greatest of three numbers.
def greatest(a , b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c 

a = 1
b = 2
c = 3
print(greatest(a, b , c)) 

#Write a python program using function to convert Fahrenheit to Celsius .
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter temperature in f: "))
c = (f_to_c(f))
print(f"{round(c,2)} °c")


#How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c", end="")
print("d", end="") # end="" this function is used to combine two lines.

#Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(n)=1+2+3+4+.....+n
sum(n)=sum(n-1)+n
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
n = int(input('enter a number: '))
print(sum(n))

#Write a python function to print first n lines of the following pattern:
#***              
#**                     - for n = 3
#*                   
def pattern(n):
    if (n==0):
        return
    print("*"* n)
    pattern(n-1) 
pattern(3)   
    
#Write a python function which converts inches to cms.
'1 cm = 2.54 inch'
def inch_to_cm(inch):
    return inch * 2.54
n = int(input("Enter the value in inch : "))
print(f"the corresponding value in cm is {inch_to_cm(n)}")

#Write a python function to remove a given word from a list and strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["harry", "rohan", "subham", "an"]
print(rem(l, "an"))

#Write a python function to print multiplication table of a given number.   
def multiple(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n = int(input("Enter the number : "))
multiple(n)       