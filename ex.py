#                           1-D ARRAY

# arr= [3,2,4,2,13]
# s=""
# for i in arr :
#     s = s+str(i)
# print(s)    


# arr = [1,2,3,4,5]
# reversed_arr = arr[::-1]
# print(reversed_arr)


# v = [1,2,3,4]
# i = 0
# j = len(v)-1
# while i<j:
#      v[i], v[j]=v[j], v[i]
#      i = i+1
#      j = j-1 
# print(v)   
     
     
     
# arr = [3,2,4,2,3]

# if arr == arr[::-1]:
#     print("yes it is palentdrome")
    
# else:
#     print("not a palentdrome")


# arr = [3,2,4,2,3]
# arr_new = arr[::-1]
# if arr == arr_new:
#     print("palentdrome")

# else:
#     print("not a palentdrome")
    
    
# arr= [3,2,4,2,3]
# s=""
# for i in arr :
#     s = s+str(i)
# print(s) 

# l1 = [3,4]
# l1*=5
# print(l1)

# x = input("Enter your number :")
# x_list = list(x)
# reversed_list = x_list[::-1]
# if x_list == reversed_list:
#     print("x is a palindrome")

# else:
#     print("not palindrome")    


# l1 = [3,4,5,6,7,8]
# for i in range (len(l1)):
#     if (i%2==0):
#         print(l1[i])
# for i in range (len(l1)):
#     if (i%2 !=0):
#         print(l1[i])

# l = [3,4,0,2,1,6]
# min = l[0]
# for i in range (1, len(l)):
#     if (l[i]<min):
#         min = l[i]
# print(min)   

# l = [3,4,0,2,1,6]
# max = l[0]
# for i in range (len(l)):
#     if (l[i]> max):
#         max = l[i]
# print(max) 

# l = [3,4,0,2,1,6]    
# min = l[0]
# max = l[0]
# for i in range (1, len(l)):
#     if (l[i]< min):
#         min = l[i]

# for i in range (1,len(l)):
#     if (l[i]> max):
#         max = l[i]  

# sum = min + max
# print(sum)

# p = min*max
# print(p)


# find second highest element
# l = [3,4,9,6,16,18,4,8]
# max = l[0]
# for i in range (len(l)):
#     if (l[i]>max):
#         max = l[i]

# min = l[0]
# for i in range (len(l)):
#     if(i>min and i<max):
#         min = l[i]
# print(min)      


# if 1 string ke saare characters same number of times dusri string mai hote hai to vo ek  
# dusre ke anagrams hote hai , if 1 zyada ya kam characters hue to vo anagrams nahi honge


# def twoSum(nums, target):
#     d = {}   # dictionary to store: number -> index

#     for i in range(len(nums)):
#         need = target - nums[i]   # what number we need

#         if need in d:             # if we already saw that number
#             return [d[need], i]   # return its index + current index

#         d[nums[i]] = i            # otherwise store this number


#                         2-D ARRAY

# n = int(input("enter rows: "))
# m = int(input("enter column: "))
# matrix = []
# for i in range(n):
#         row = []
#         for j in range(m):
#                 var = int(input("enter your marks: "))
#                 row.append(var)
#         matrix.append(row)
# print("matrix :")
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print() 


#     # this concept is for printing only diagonal element  
# for i in range(n):
#       for j in range(m):
#             if i == j:
#                   print(matrix[i][j], end=" ")
#             else:
#                   print(end=" ")
# print()      


# n = int(input("enter a number : "))
# def odd_to_even(n):
#     if (n%2==0):
#         print("even")
#     else:
#         print("odd")
# odd_to_even(n)  


# class node:
#     def __init__(self,data=None,next=None, prev=None):
#         self.data=data
#         self.next=next
#         self.prev=prev

# class DLL:
#     def __init__(self, head=None):
#         self.head=head

#     def insert_at_beginning(self,data):
#         new_node=node(data)
#         if self.head is None:
#            self.head=new_node
#            return
        
#         new_node.next=self.head
#         self.head.prev=new_node
#         self.head=new_node

#     def insert_at_end(self,data):
#         new_node=node(data)
#         if self.head is None:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next

#         temp.next=new_node
#         new_node.prev=temp

#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.data,end=" <-> ")
#             temp=temp.next
#         print("None")

# l1 = DLL()
# l1.insert_at_beginning(100)
# l1.insert_at_beginning(10)
# l1.display()


# class Node:
#   def __init__ (self, data = None, next=None, prev=None):
#     self.data=data
#     self.next=next
#     self.prev=prev
# class DLL:
#   def __init__ (self, head=None):
#     self.head=head

#   def insert_at_Begining(self, data):
#     new_node=Node(data)
#     if self.head is None:
#       self.head=new_node
#       return


#     new_node.next=self.head
#     self.head.prev=new_node
#     self.head=new_node

#   def insert_at_End(self, data):
#     new_node=Node(data)
#     if self.head is None:
#       self.head=new_node
#       return

#     temp=self.head
#     while temp.next:
#       temp=temp.next

#     temp.next=new_node
#     new_node.prev=temp

#   def insert_at_pos(self, data, val):
#     if self.head is None:
#       print("List is empty")
#       return

#     temp=self.head
#     while temp.next and temp.data!=val:
#       temp=temp.next
    
#     new_node=Node(data)
#     new_node.next=temp.next
#     new_node.prev=temp
#     temp.next.prev=new_node
#     temp.next=new_node

#   def display(self):
#     temp=self.head
#     while temp:
#       print(temp.data, end=" <-> ")
#       temp=temp.next
#     print("None")

# l1=DLL()
# l1.insert_at_Begining(100)
# l1.insert_at_Begining(10)
# l1.insert_at_End(-11)
# l1.insert_at_pos(91,100)
# l1.display()


# # <----- Implementation of Stack using List ----->
# class Stack:
#     # <----- Creating Constructor for Stack Initialization ------>
#     def __init__ (self):
#         self.stack = []

#     # <----- Inserting an Element ----->
#     def push(self, data):
#         self.stack.append(data)

#     # <----- Removing an Element ----->
#     def pop(self):
#         if len(self.stack)==0:
#             print("UnderFlow")
#             return
#         self.stack.pop()
    
#     # <----- Clecking Top Element ----->
#     def peek(self):
#         if len(self.stack)==0:
#             print("UnderFlow")
#             return
#         print(self.stack[-1])
    
#     # <----- Checking stack is Empty or Not ----->
    
#     def empty(self):
#         if len(self.stack)==0:
#             print("Stack is Empty")
#         else:
#             print("Stack is Not Empty")

#     # <----- checking the size of the stack ----->
    
#     def size(self):
#         print(len(self.stack))

# # <----- Creating an Object of Stack class----->
# s = Stack()
# s.push(14)
# s.empty()
# s.peek()
# s.pop()
# s.peek()
# s.pop()
# s.empty()

