friends = ["Apple", "Orange", "5", "345.06", "Manav", "Kunal", "False"]
print(friends[0])
                  #list are mutable they can be change , but strings are immutable .
friends[0] = "Grapes"
print(friends[0])  # here'[0]'specifies the number of data in the list. like [0]=apple, [6]=false

print(friends[1:4]) #slicing in list is same as string.(0,1,2,3,....,n)

#print(friends[start : end : steps to skip])

#list is mutable unlike strings , jaise string harr baar changes par new banti hai but agar hum purani likhe to string vahi same rehti hai
# but list haar bar changes par vo new banti hai if uski purani value likhe to vo same nahi rahegi 
# tabhi list mutable hoti hai 
#list ki bhi list bana skte hai allowed hai 
print(friends)