#Arithematic operators(+,-,/,*)
a = 7
b = 4
c = a+b 
print(c)

#Assingment opertors(=,+=,-=)
a = 4-2 #assing 4-2 in a
print(a)
b = 6
b += 3 #increment the value of b by 3 and then assing it to b
# can also use b -= 3 increament will become decrement
print(b)

#comparison operators(==,>,>=,<,!=)
d = 5<4
print(d)
e = 5>4
print(e)
f = 5>=4
print(f)
g = 5<=4 # <=,>= less than equal to , greater than equal to
print(g)
h = 5!=4 # != is not equal to
print(h)
i = 5==4 # ==  means if they are equal 
print(i)
print("\n"*1)


# logical operators(and,or,not)
j = True or False
# truth table of 'or'
print( "True or False is", True or False)
print("True or True is", True or True)
print("False or True  is", False or True)
print("False or False is", False or False)

print("\n"*2)

#truth table of 'and'
print( "True and False is", True and False)
print("True and False is", True and True)
print("True and False is", False and True)
print("True and False is", False and False)
print()
#not operators will print true as false and false as true
print(not(True))
print(not(False))

#type function:- used to change the type of a function if valid.
k = 31
t = type(k) #class <int> integer
print(t)
l = "31"
t = type(l) #class <str> string
print(t)
m = "31.2"
n = float(m) # a is a string but i want it to be float 
t = type(n)
print(t)