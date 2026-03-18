#METHOD 1 :- COUNT
a = (1,2,3,4,5,"surya",False, 5,5)
no = a.count(5) #counts the number of times the data is written
print(no) 

#METHOD 2 :- INDEX
b = (1,2,3,4,5,"surya",False, 5,5)
bo = a.index(5) # will find the index number where the given data is present and when it will find then it will stop finding after.
print(bo)

#METHOD 3 :- CONCATENATION
c = (1,2,3,4)
d = (5,6,7,8)
concatenated = c+d # '+' sign is used it combines to tuple
print(concatenated)

#METHOD 4 :- REPETATION
e = (1,2,3)
repeat = e*3 # repeats the tuple by number of times you multiply, sign:- '*' .
print(repeat)

#METHOD 5:- MEMBERSHIP, used to check if the value is in tuple or not. 
f = (1,2,3,4)
print(2 in f) # output ; true
print(5 in f) # output ; false
 