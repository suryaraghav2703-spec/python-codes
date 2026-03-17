# METHOD 1 :- APPEND
friends = ["Apple", "Orange", "5", "345.06", "Manav", "Kunal", "False"]
print(friends)
friends.append("surya") # append mai ek new data ko list ke end mai likh dega
print(friends)

#METHOD 2 :- SORT
l1 = ["1", "5", "4", "7", "3"]
l1.sort() # sort method assending order mai numbers ko sort kardeta hai 
print(l1)

#METHOD 3 :- REVERSE
l2 = ["1", "34", "64", "45", "5", "7"]
l2.reverse() # reverse the data not in  any order like asending or decending it just reverse the data.
print(l2)

#METHOD 3 :- INSERT 
l3 = ["1", "34", "45", "63", "6", "7"]
l3.insert(4,333) # here insert puts the number in the list, first put of which index you want to put data then the number which you wanna insert.
print(l3)

# METHOD 4 :- POP 
l4 = ["1", "34", "6", "22", "3", "6", "7"]
l4.pop(4) # it will pop out the value of the index you put in .
print(l4) 
print(l4.pop(4)) # pop method can also be written in this it will show which value they pop out from the list.

#METHOD 5 :- REMOVE 
l5 = ["1", "23", "45", "21", "6", "7"]
l5.remove("21") #removes the data which you want to delete from the list.
print(l5)

