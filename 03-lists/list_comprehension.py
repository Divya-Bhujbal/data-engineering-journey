"""
=========================================================
Topic        : List Comprehension
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered

✔ What is List Comprehension?
✔ Syntax
✔ Basic Examples
✔ if Condition
✔ if-else Expression
✔ Nested Loops
✔ Nested List Comprehension
✔ Common Interview Questions
✔ Quick Revision

=========================================================
"""

#1. What is List Comprehension

"""
List comprehension is a concise way to create a new list
by writing a single line of code instead of using a traditional loop.

It makes code shorter, cleaner and more readable.
"""

#2. Syntax

# Traditional way 

a = [1,2,34,5]
b = []
for i in a :
    b.append(i*i)
print("New list : ",b)



# List comprehension method : single line code 

c = [1,23,5,67]
d= [num*num for num in c]
print("New list : ",d)


# 3. if condition

# traditional way 
a = [1,2,3,45,6,78]
b =  []
for num in a:
    if num%2==0:
        b.append(num)
print("If statement result : ",b)


# List comprehension method

list1 = [1,2,34,56,78]
new_list = [num for num in list1 if num%2==0]
print("List Comprehension method : ", new_list)



#4. if-else Expression

c = [2,'v',3,5]
d = [2,'v',3,5]

if c is d:
    print("c is d")
else :
    print("c is not d")


# List comprehension method
list_new = [2,3,45,6,9]
b = ["even" if num%2==0 else "odd" for num in list_new]
print("List comprehension method :- ",b)



#5. Nested Loops 

numbers = [2,3,6,12,34,78,9]
new_list = []
for num in numbers :
    if (num %2==0):
        if (num%3==0):
            new_list.append(num)
    else :
        print('No is not divisible by 6')

print(f"List of nums divisible by 6 : {new_list}")
print("Length of new list : ",len(new_list))



# List comprehension method
numbers_1 = [2,34,567,89,0,98]
pairs = [(x,y) for x in [1,2,65] for y in [3,4]]
print("pairs : ",pairs )


# 6. Common Interview Questions

"""

Q1. Why use list comprehension?

Answer:
Cleaner and more concise code.

--------------------------------------

Q2. Does list comprehension create a new list?

Answer:
Yes.

--------------------------------------

Q3. Is list comprehension faster than a for loop?

Answer:
Generally yes, because it is optimized internally in Python.

--------------------------------------

Q4. Can we use if and else together?

Answer:
Yes.

Syntax:

[expression_if_true if condition else expression_if_false for item in iterable]

--------------------------------------

Q5. Can list comprehension replace every for loop?

Answer:
No.

Use normal loops when logic becomes too complex.

"""


# 7. Quick Revision

"""✔ Creates a new list

✔ Shorter than a for loop

✔ More Pythonic

✔ Supports if conditions

✔ Supports if-else expressions

✔ Supports nested loops

✔ Frequently asked in interviews

✔ Commonly used in Data Engineering"""




