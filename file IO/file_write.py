st = "hey yo this language is amazing"

f = open("myfile.txt", "w")

f.write(st)

f.close()

# more functions
f = open("file.txt")

line = f.readline() # jitni baar ye karoge utni baar vo lines ko read karega 
print(line, type(line))

# line1 = f.readlines() 
# print(line1, type(line1))

# line2 = f.readline2() 
# print(line2, type(line2))

# line3 = f.readline3() 
# print(line3, type(line3))
line = f.readlines()
while(line != ""):     # fore simple way to write. 
    print(line)
    line = f.readline()

f.close()




