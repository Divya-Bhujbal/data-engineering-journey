"""
=========================================================
Topic        : List Methods
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered

✔ append()
✔ extend()
✔ insert()
✔ remove()
✔ pop()
✔ clear()
✔ index()
✔ count()
✔ reverse()
✔ sort()
✔ copy()

✔ Quick Revision

=========================================================
"""

#1. append() - 
# Adds a single object to the end of the list.
# The object is added as it is (it is not unpacked).

my_list = [9,"l",'m',0.9]
my_list.append("project")
print("Append : ",my_list)


my_list2 = [4,6]
my_list2.append([45,"My_work"])
print("Append 2 : ",my_list2)

#2. extend() 
# Adds all elements from an iterable to the end of the list.
# It iterates over the iterable and appends each element individually.
# extend() accepts any iterable, not just lists

my_list1 = [9,8,0,9]
my_list1.extend("12")
print(my_list1)

my_list2 = [4,6]
my_list2.extend([45,"My_work"])
print("Extend : ",my_list2)

numbers = [1, 2]
numbers.extend((3, 4))
print(numbers)

#3. insert() -  insert the elements @specified index ---> list_name.insert(index_no,value)
# Existing elements shift to the right.

Fruits = ['mango','banana']
Fruits.insert(1,"grapes")
print("Fruits : ",Fruits)


#4. remove() - ----> list_name.remove(value)
# Removes the first occurrence of the specified value.
# Raises ValueError if the value is not present.

Fruits = ['a','b','c','d','e']
Fruits.remove('b')
print("Fruits after removing ", Fruits)


#5. pop() - remove the last element if index is not provided - gives error if index out of range ----> list_name.pop(index)

Fruits.pop(1)
Fruits.pop()
print(Fruits)


#6. clear() - clear all the elements ,makes list empty

Fruits.clear()
print(Fruits)


#7.index()

elements =['a',1,34,0.9,'a']  # returns index of the first occurrence, Raises ValueError if the value is not found.
print("Index " ,elements.index('a'))


#8.count() #Count Occurrences of a Specific Item

print("Count :",elements.count('a'))


#9.reverse() - reverse the list'
# Modifies the original list.
# Returns None.

a=[2,4,'h','divya']
a.reverse()
print("Reverse the list : ",a)



#10.sort() 
# Sorts the list in ascending order.
# All comparable elements should be of compatible types.
# Modifies the original list.


a=[3,4,678,9,9.3]
a.sort()
print("sorted a : ",a)

b=['k','d','w']
b.sort()
print("sorted b : ",b)



#11 copy() - create new object with the same values
print(id(b))
c = b.copy()
print(id(c))
print(c)



#!2 Quick Revision

"""
✔ append() → Add one object

✔ extend() → Add elements from an iterable

✔ insert() → Insert at a given index

✔ remove() → Remove by value

✔ pop() → Remove by index and return value

✔ clear() → Remove all elements

✔ index() → Find first occurrence

✔ count() → Count occurrences

✔ reverse() → Reverse in place

✔ sort() → Sort in place

✔ copy() → Create shallow copy

"""




