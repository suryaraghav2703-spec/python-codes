#q.) Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("enter your name:")
print(f"good afternoon {name}")# "f" function marks the variables put in curly bracket 


# q.) Write a program to fill in a letter template given below with name and date.
letter = '''Dear  <| Name|>, 
 You are selected!
<|Date|>'''
print(letter.replace(" <| Name|>", "surya").replace("<|Date|>", "10 0ctober 2025"))


#q.)Write a program to detect double space in a string.
a = "surya is a good   boy"
print(a.find("  "))
print(a.find("go"))#find is used to find the in which index the word is given


#q.) Replace the double space from problem 3 with single spaces.
b = "surya is a good   boy and"
print(b.replace("   ", " "))

#q.) Write a program to format the following letter using escape sequence characters.
letter ="Dear surya, \n\tThis python course is nice.\n Thanks!"
print(letter)