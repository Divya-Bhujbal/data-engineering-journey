"""
Data Type

1. A data type defines the kind of value an object stores and
    the operations that can be performed on it.

2. Every object in Python has a data type.

3. The type of an object can be determined using the type() function.

"""


"""
1. Built-in Data Types

"""

name = "Divya"
age = 23
salary = 12345.7
is_active = True
numbers = [1, 2]
subjects = ("Python", "SQL")
student = {"name": "Divya"}
unique_numbers = {1, 2, 3}
matrix = [[1, 2], [3, 4]]
complex_number = 2 + 3j
value = None

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))
print(type(numbers))
print(type(subjects))
print(type(student))
print(type(unique_numbers))
print(type(matrix))
print(type(complex_number))
print(type(value))




"""
2. Mutable and Immutable Data types

"""
"""

Immutable  - object cannot be modified after it is created.
---------
int
float
bool
complex
str
tuple
NoneType

Mutable - object can be modified after it is created.
-------
list
dict
set
"""
# Immutable Example

code =  "Python"
print(id(code))
code = code + " Programming"
print(id(code))              # A new string object is created.The original string is not modified.



# Mutable Example 
list = ['a','b','c']
print(id(list))
list.append('d')
print(list)           # The original string is modified.
print(id(list))

