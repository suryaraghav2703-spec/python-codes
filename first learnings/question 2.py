#q2.) Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os 

# select the directory whose content you want list
directory_path = '/'

# use the os module to list the directory Content
contents = os.listdir(directory_path)

# print the content of the directory 
print(contents)
