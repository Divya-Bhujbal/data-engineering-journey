"""
=========================================================
Topic        : Data Types
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered
--------------
✔ What is a Data Type?
✔ Built-in Data Types
✔ Mutable vs Immutable Objects
✔ type()
✔ isinstance()
✔ Type Conversion
✔ Implicit vs Explicit Type Conversion
✔ Truthy & Falsy Values
✔ Common Interview Questions

=========================================================
"""

# =====================================================
# 1. What is a Data Type?
# =====================================================

"""
Data Type

1. A data type defines the kind of value an object stores
   and the operations that can be performed on it.

2. Every object in Python has a data type.

3. The type of an object can be determined using type().
"""

# =====================================================
# 2. Built-in Data Types
# =====================================================

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

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of salary:", type(salary))
print("Type of is_active:", type(is_active))
print("Type of numbers:", type(numbers))
print("Type of subjects:", type(subjects))
print("Type of student:", type(student))
print("Type of unique_numbers:", type(unique_numbers))
print("Type of matrix:", type(matrix))
print("Type of complex_number:", type(complex_number))
print("Type of value:", type(value))

"""
Built-in Data Types

Immutable
---------
int
float
bool
complex
str
tuple
NoneType

Mutable
-------
list
dict
set
"""

# =====================================================
# 3. Mutable vs Immutable Objects
# =====================================================

"""
Immutable Objects

Objects cannot be modified after creation.

Examples:
int
float
bool
complex
str
tuple
NoneType
"""

code = "Python"

print(id(code))

code = code + " Programming"

print(id(code))
print(code)

"""
Notice:

A new string object is created.
The original string object is not modified.
"""

print()

"""
Mutable Objects

Objects can be modified after creation.

Examples:
list
dict
set
"""

letters = ["a", "b", "c"]

print(id(letters))

letters.append("d")

print(id(letters))
print(letters)

"""
Notice:

The id() remains the same.

The existing list object is modified.
"""

# =====================================================
# 4. type()
# =====================================================

"""
type()

Returns the type (class) of an object.
"""

print(type(10))
print(type(10.5))
print(type(True))
print(type("Python"))
print(type([1, 2, 3]))

# =====================================================
# 5. isinstance()
# =====================================================

"""
isinstance()

Checks whether an object belongs to a given type or class.
"""

x = "Python"

print(isinstance(x, str))
print(isinstance(x, int))
print(isinstance(x, (int, str)))
print(isinstance(x, int | str))      # Python 3.10+

# =====================================================
# 6. Type Conversion
# =====================================================

"""
Type Conversion

Converting one data type into another.

Two Types

1. Implicit Type Conversion
2. Explicit Type Conversion
"""

# Explicit

age = "23"

print(int(age))

price = "123.45"

print(float(price))

number = 100

print(str(number))

print(bool(1))
print(bool(0))

# =====================================================
# 7. Implicit Type Conversion
# =====================================================

"""
Python automatically converts one type
to another whenever it is safe.
"""

a = 10
b = 2.5

print(a + b)

"""
Output

12.5

Python converts int into float automatically.
"""

# =====================================================
# 8. Truthy & Falsy Values
# =====================================================

"""
Falsy Values

False
None
0
0.0
''
[]
{}
set()

Everything else is Truthy.
"""

print(bool(""))
print(bool([]))
print(bool({}))
print(bool(0))
print(bool(None))

print(bool("Python"))
print(bool([1]))
print(bool(10))

# =====================================================
# 9. Common Interview Questions
# =====================================================

"""
Question 1

What is the difference between type() and isinstance()?

Answer

type()

Checks the exact type.

isinstance()

Checks the type and inheritance.
"""

"""
Question 2

Difference between Mutable and Immutable objects?

Mutable
-------
Can be modified.

Immutable
---------
Cannot be modified after creation.
"""

"""
Question 3

Difference between Implicit and Explicit Type Conversion?

Implicit

Done automatically by Python.

Explicit

Done by the programmer using:

int()
float()
str()
bool()
"""

# =====================================================
# 10. Coding Challenge
# =====================================================

"""
Predict the output before running.
"""

name = "Python"

print(id(name))

name += "3"

print(id(name))

print()

numbers = [1, 2]

print(id(numbers))

numbers.append(3)

print(id(numbers))

# =====================================================
# 11. Quick Revision
# =====================================================

"""
Quick Revision

✔ Every object has a data type.

✔ type() returns the object's type.

✔ isinstance() checks whether an object belongs to a type.

✔ Mutable:
    list
    dict
    set

✔ Immutable:
    int
    float
    bool
    complex
    str
    tuple
    NoneType

✔ Explicit Type Conversion:
    int()
    float()
    str()
    bool()

✔ Implicit Type Conversion:
    Done automatically by Python.

✔ Mutable objects modify the existing object.

✔ Immutable objects create a new object when modified.
"""