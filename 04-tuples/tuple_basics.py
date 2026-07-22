"""
=========================================================
Topic        : Tuple Basics
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered

✔ What is a Tuple?
✔ Creating Tuples
✔ Ordered Collection
✔ Immutable Nature
✔ Heterogeneous Data
✔ Duplicate Values
✔ Packing
✔ Unpacking
✔ Indexing
✔ Negative Indexing
✔ Slicing
✔ Iteration
✔ enumerate()
✔ len()
✔ Membership Operator (in, not in)
✔ Tuple vs List
✔ Common Interview Questions
✔ Quick Revision

=========================================================
"""


#1. What is a Tuple?
# A tuple is an ordered, immutable collection that can store multiple objects of different data types.

# Tuples allow duplicate values and support:
# 1. Indexing
# 2. Slicing
# 3. Iteration


a = ('a',1,2.3)
print(a)
print(type(a))




#2. Creating tuples 

a = ('a',1,2.3)
print(a)
print(type(a))


# single element tuple 
b = (30)
print("Type of b is : ", type(b)) # <class 'int'>

b = (30,)
print("Type of b is : ", type(b)) # <class 'tuple'>

# empty tuple 

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))  # tuple


#3.Ordered collection
# Tuples preserve insertion order.

print(a[0])
print(a[1])
print(a[2])

#4.Immutable nature

# a[1] = 3

# TypeError:
# 'tuple' object does not support item assignment

#5.Heterogeneous Data

b = (9,'m',0.8,"divya")
print(b)



#6. Duplicate values 
c =  ('a','a') #it allows duplicate values to store
print(c)



#7. Packing
# Packing means storing multiple values inside a tuple.

student = ("Divya",23,"Bhujbal")


#8. Unpacking

name,*age,surname = student
print("Name " ,name)
print("Age ",*age)
print("Surname ",surname)


#9. Indexing and slicing

# Positive Indexing
student = ("Divya",23,"Bhujbal",'k')
print(student[0]) # 0 th index
print(student[1]) # 1 st index
print(student[0:3]) # start point ---> 0 th index , end point --->3 rd index (exclusive)
print(student[0:4:2]) # start point - 0 , end point - 4 (exclusive), step 2 


# Negative Indexing 

print(student[-1]) # 1 st index from the end 
print(student[-4:-1])
#reverse of a tuple
print("Reverse of a tuple : ", student[::-1])

#10. Iteration 

for i in student :
    print(i ,end = " ")


#11.enumerate()  --->   print index+value
print("\n") #new line
for idx,value in enumerate(student) :
    print(idx," : ", value)


#12.len()

print("Length of a tuple : ", len(student))


#13.Membership Operator (value in/not in tuple)   ---> returns boolean 
print("divya" not in student)
print("Divya" in student)
print("Python" in student)


#14.Tuple vs List
"""List

✔ Mutable

✔ Uses []

✔ More methods

✔ Suitable when data changes

Tuple

✔ Immutable

✔ Uses ()

✔ Only count() and index()

✔ Suitable for fixed data"""


#.15 Tuple Concatenation

a = (1,'m',6.70)
b = ('divya',110)
print("Tuple concatenation ",a+b)


#16. Tuple Repetition
print("Tuple Repetition ",a*2)


#17.max(), min(), sum()

d = (2,3,4,6,1322)
print("max ",max(d))
print("min ",min(d))
print("sum ",sum(d))



#18. Nested tuple

a = (('a',1),('b',2))
print(a[0])
print(a[0][1])


#19. Interview Questions

"""
Q1. Why are tuples immutable?

Answer

To make them safe for fixed data and allow them to be hashable.

------------------------------------

Q2. Can tuples contain mutable objects?

Answer

Yes.

Example

([1,2],3)

The tuple is immutable,
but the list inside it can change.

------------------------------------

Q3. Can a tuple be used as a dictionary key?

Answer

Yes,

provided all its elements are hashable.

------------------------------------

Q4. List vs Tuple?

(Most common interview question.)"""


#20. Quick Revision
"""

✔ Ordered

✔ Immutable

✔ Allows duplicate values

✔ Supports heterogeneous data

✔ Supports indexing

✔ Supports slicing

✔ Supports iteration

✔ Supports packing & unpacking

✔ Supports concatenation

✔ Supports repetition

✔ Indexing → O(1)

✔ Slicing → O(k)"""

