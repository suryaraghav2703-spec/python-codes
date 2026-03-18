#a for loop is used to iterate through a sequence like list,tuple,or string[iterables]
l = [1,2,3,4,5]
for item in l:
    print(item)

#RANGE FUNCTION IN PYTHON
#it is used to generate a sequence of a number. we can also specify the start,stop, and step-size 
for i in range(0,7): #range(7) can also be used
    print(i) # output will print 0 to 6 

#FOR LOOPS WITH ELSE
l = [1,7,8]
for item in l:
    print(item) 
else:
    print("done") # this is printed when he loop exhausts!     

#break and continue
for i in range(100):
    if(i==34):
        break #exit the loop right now
    print(i) 

for i in range(100):
    if(i==34):
        continue #skip this iteration
    print(i)

#pass:- is a null statement in python.it instructs "to do nothing".
for i in range(645):
    pass
    i = 0
    while(i<45):
        print(i)
        i = i+1
    