#METHOD 1 :- ITEMS
marks = {
    "surya": 100,
    "subham": 56,
    "kunal": 23,
    0: "harry"
}

print(marks.items()) #right hand side par jo bhi ho vo show hoga

#METHOD 2:- KEYS
marks = {
    "surya": 100,
    "subham": 56,
    "kunal": 23,
    0: "harry"
}
print(marks.keys())#left hand side par jo bhi show ho vo hoga

#METHOD 3:- UPDATE
marks = {
    "surya": 100,
    "subham": 56,
    "kunal": 23,
    0: "harry"
}
marks.update({"surya":99})#will update the dictionary
print(marks)

#METHOD 4:- GET
marks = {
    "surya": 100,
    "subham": 56,
    "kunal": 23,
    0: "harry"
}

print(marks.get("surya")) 
#print(marks.get("surya2")) it prints "NONE"if the written and items are not same. 
#print(marks["surya2"]) it returns "AN ERROR".

#METHOD 5:- clear
#dict.clear() clears the dictionary

#METHOD 6:- copy
#dict.copy() returns a shallow copy of the dictionary





