"""
=========================================================
Topic        : List Basics
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered

✔ What is a List?
✔ Creating Lists
✔ Ordered Collection
✔ Mutable Nature
✔ Heterogeneous Data
✔ Duplicate Values
✔ Indexing
✔ Negative Indexing
✔ Slicing
✔ Iterating over Lists
✔ enumerate()
✔ len()
✔ Membership Operator (in, not in)
✔ Updating Elements
✔ Deleting Elements
✔ Common Interview Questions
✔ Quick Revision

=========================================================
"""


# 1 . What is the list ?
# A list is an ordered, mutable collection that can store multiple objects of different data types.

# Lists allow duplicate values and support:
# 1. Indexing
# 2. Slicing
# 3. Iteration



My_list = ['a','b','A','a','']
print("My list is : ", My_list)
print(type(My_list))



#2 . Creating lists
empty_list = []
print("Empty list : " , empty_list)


My_list = ['a','b','A','a','',1,2.3,"Apple",[1,2]]
print("My list is : ", My_list)


#3 . Ordered Collection 
# Lists preserve insertion order.
print(My_list[0])
print(My_list[1])
print(My_list[2])


#4. Mutable Nature
print(id(My_list))

My_list[0] = "Replaced_item"

print(id(My_list))

# Same id because the existing object is modified.


#5. Heterogeneous Values

my_list = [1,'a',"h",56.7,"Divya"]
print(my_list)


#6. Duplicate Values

my_list1 = [1,1,2,3,4,5,6,7,8,9,5]
print(my_list1)


#7.Indexing

print(my_list1[0])
print(my_list1[1])
print(my_list1[3])



#8. Negative indexing

print(my_list1[-1])
print(my_list1[-2])


#9. Slicing

print(my_list1[0:3])
print(my_list1[0:3:2])
print(my_list1[::-1]) #reverse 


#10. Iterating over Lists

list1 = ['a','b','c']
for i in list1:
    print("Iterating over lists ",i)


#11. enumerate()

list1 = ['a','b','c',2,3,1]
for index,value in enumerate(list1):
    print(index ," : " ,value)


#12.len() 

print("Length of list : ", len(list1))


#13.Membership Operator (in, not in)- returns True/False

print('a' in list1)

print(34 in list1)

print('a' not in list1)

print(100 not in list1)


#14.Updating Elements

list2 = [1,2,3]
list2[2]=30 # replace 3 with 30
print("List with updated element : ",list2) # Lists are mutable, so elements can be modified.


#15.Deleting Elements - remove(element)

list3 = [1,23,4,8.3,'a']
del list3[0]
print(list3)

#16.Nested list

matrix = [
    [1,2,3],
    ["a",'b',7.8]
]

print("matrix : ",matrix)
print("matrix : ",matrix[1])
print("matrix : ",matrix[0][0])


#17.List Index Out of Range

numbers = [10,20,30]

# print(numbers[5])
# numbers[3]=40

# IndexError: list index out of range

#18.
"""
Interview Notes

✔ Lists are mutable.

✔ Lists preserve insertion order.

✔ Lists allow duplicate values.

✔ Lists support heterogeneous data.

✔ List indexing -> O(1)

✔ List slicing -> O(k)

✔ Lists are implemented as dynamic arrays.

"""