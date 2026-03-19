#q1.)write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up!
words = {
    "madad": "help",
    "kursi": "chair",
     "billi": "cat"
}
word = input("enter the word you want meaning of:")
print(words[word])

#q2.)write a program to input eight numbers from the user and disply all the unique number (once).
s = set()
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
n = input("enter number :")
s.add(int(n))
print(s)

#q3.)can we have a set with 18(int) and "18"(str) as a value in it?
r = set()
r.add(18)
r.add("18")
print(r) #output :- yes we can have 18 as integer and string in the value of set

#q4.)create an empty dictionary. allow 4 friends to enter their favorite language as value and use key as their names. assume that the names are unique
d ={}
name = input("enter friends name: ")
lang = input("enter language name: ")
d.update({name: lang})

name = input("enter friends name: ")
lang = input("enter language name: ")
d.update({name: lang})

name = input("enter friends name: ")
lang = input("enter language name: ")
d.update({name: lang})

name = input("enter friends name: ")
lang = input("enter language name: ")
d.update({name: lang})

#q6.)can you change the values inside a list which is contained in set s?
s = {8,7,12,"surya",[1,2]}
# no you cannot change a set also you cannot add list in a set
