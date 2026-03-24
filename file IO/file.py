'''
a = " a very long string with emails"
email = []
3 seconds
isme hoga ye ki jab code run kiya to emails aayi but jab exit kiya to emails bhi gayab 
to ab ye emails gayab na ho isliye hum issey FILES mai save karte hai 
'''
f = open("file.txt", "r")
data = f.read()
print(data)
f.close() # close karna bahut important hai 
# type of Files 
# 1.) text files like .txt
# 2.) binary files like .jpg , .dat, etc
# r -> open for reading
# w -> open for writing 
# a -> open for appending
# + -> open for updating
# 'rb' will open for read in binary 
# 'rt' will open for read in binary 


