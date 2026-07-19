#Variables 

# 1. Variables in python store references to the objects 
# 2. A reference is a value stored in a variable that points to an object. 
# 3. Variables in Python do not contain the object itself; they hold references to objects.

"""1. Variable Naming Convemtion"""

"""
=========================================================
Variable Naming Convention
=========================================================

Python follows PEP 8 (Python Enhancement Proposal 8) style guide
for naming variables.

Rules
-----

1. Variable names can contain:
   - Letters (A-Z, a-z)
   - Digits (0-9)
   - Underscore (_)

2. Variable names cannot:
   - Start with a digit
   - Contain spaces
   - Contain special characters like @, #, $, %, etc.

3. Variable names are case-sensitive. """

# In below example variables are employee_name,MAX_RETRY,Student (Variable which refers to a class object )

employee_name = "Divya"

MAX_RETRY = 3

class Student:
    pass



"""2. Multiple Assignment """
a,b,c = 10,20,30
print("Multiple Assignment a: " , a)  #10
print("Multiple Assignment b: " , b)  #20
print("Multiple Assignment b: " , c)  #30




"""3. Swapping Variables """

a = 10
b = 20

print("Before Swapping a: ", a)
print("Before Swapping b: ", b)

a,b = b,a

print("After Swapping a: ", a)
print("After Swapping b: ", b)



"""4. Dynamic Typing """
# Variables don't have a fixed type.
# Objects have types.

#same variable name with different types
x = 10

print(type(x))  #int

x = "Python"

print(type(x)) #string

x = 3.14

print(type(x)) #float



"""5. isinstance()"""

# a built-in Python function used to check if an object belongs to a specific class, data type, or a subclass thereof
# will cover in inheritance later ,just look at the example and o/p

x = "a"

print("Isinstance a string ? : ", isinstance(x,str))

print("Isinstance a int ? : ", isinstance(x,int))

# check whether belongs to any of the instances

print("Isinstance a int or str  ? : ", isinstance(x,int|str))

print("Isinstance a int or str  ? : ", isinstance(x,(int , str)))



"""6. Variables are Labels (Not Boxes)

Many beginners think variables store values.

Python variables are actually labels (or names) that refer to objects.

Example:

x = 10

Python creates an integer object (10) and x refers to it.

Visual Representation

x
│
▼
10

The variable does not contain the integer.
It simply points (references) to the integer object.
"""


"""7. Every Python Object has Three Properties

Every object in Python has:

1. Identity
    - Unique identifier of the object.
    - Obtained using id()

2. Type
    - Type of the object.
    - Obtained using type()

3. Value
    - Actual data stored inside the object.

Example
"""

x = [1,2,3]

print("Identity :", id(x))
print("Type :", type(x))
print("Value :", x)




"""8. type()

type() returns the type (class) of an object.
"""

a = 10
b = 10.5
c = "Python"
d = True

print("class of a",type(a))
print("class of b",type(b))
print("class of c",type(c))
print("class of d",type(d))



"""9. Immutable Objects

Some objects cannot be modified after creation.

Examples:
- int
- float
- bool
- str
- tuple

Example:
"""

name = "Python"

# This creates a NEW string object.
name = name + " Programming"

print(name)


"""10. Mutable Objects

Mutable objects can be modified after creation.

Examples:
- list
- dictionary
- set
"""

numbers = [1,2,3]

numbers.append(4)

print(numbers)




"""11. Variables can refer to different objects during execution."""

x = 10

print(x)

x = "Python"

print(x)    

x = [1,2,3]

print(x)

"""
The variable x is the same.

Only the object it refers to changes.
"""


"""12. None

None represents the absence of a value.

None is also an object in Python.
"""

x = None

print(x)

print(type(x))

print(x is None)




"""13. Common Interview Mistake"""

a = [1,2]

b = a

c = a.copy()

print(a is b)
print(a is c)

"""
Remember:

b = a
Copies the reference.

copy()
Creates a new object.

Many beginners think both statements behave the same.

They do not.
"""
"""----------------------------------------------------------------------------------------------------------------------------"""
# This example demonstrates that modifying a mutable object
# through one variable affects all references to that object.   

a = [1,2,3]
b = a
b.append(3)
print("Result of a: ", a)
print("Result of b: ",b)

"""
a ───┐
     │
     ▼
   +--------+
   | [1, 2] |
   +--------+
     ▲
     │
b ───┘         

b.append(3)
             ---->
a ───┐
     │
     ▼
 +-----------+
 | [1,2,3]   |
 +-----------+
     ▲
     │
b ───┘

"""
"""----------------------------------------------------------------------------------------------------------------------------"""

# Why doesn't Python copy the list?
"""
Suppose the list has 10 million elements.
If Python copied it every time you wrote:
b = a
it would be:1) slow
            2) memory-intensive

Instead, Python simply copies the reference, which is very efficient."""


"""----------------------------------------------------------------------------------------------------------------------------"""



#
a = [1, 2]
b = a

print(id(a))  
print(id(b))

# both id's are same , i.e. same object 

"""----------------------------------------------------------------------------------------------------------------------------"""

a = [1,2]
b = [1,2]

print(id(a))
print(id(b))

# both id's are different now ,changing one would not reflect changes in the other , diff objects 


"""----------------------------------------------------------------------------------------------------------------------------"""
# challenge 1 : try to answer by your own (Hint is given, use it only if needed)
a = [10, 20]
b = a                # both variables refer to the same object.
c = a.copy()         # create new object with same value

print(a is b)   # compares reference i.e. if both variables refer to the exact same object
print(a is c)   # compares reference i.e. if both variables refer to the exact same object
print(a == c)   # compares values i.e. whether two objects have the same value by calling their equality method

# challenge 2 : try to answer by your own (Hint is given, use it only if needed)

a = [1, 2]    
b = a          # both variables refer to the same object.
b = [3, 4]     #very imp - You are not modifying the original list.Instead, you're making b refer to a new list object.

print(a)
print(b)
print(a is b)


# challenge 3 : try to answer by your own (Hint is given, use it only if needed)

a = [1, 2]
b = a         # both variables refer to the same object.

b = b + [3]   # create new object

print(a) 
print(b)
print(a is b)

"""----------------------------------------------------------------------------------------------------------------------------"""


# Takeaway 


"""
| Code        | Changes existing object? | Creates new object? |
| ----------- | :----------------------: | :-----------------: |
| `append()`  |           ✅ Yes          |         ❌ No        |
| `extend()`  |           ✅ Yes          |         ❌ No        |
| `sort()`    |           ✅ Yes          |         ❌ No        |
| `reverse()` |           ✅ Yes          |         ❌ No        |
| `copy()`    |           ❌ No           |        ✅ Yes        |
| `+`         |           ❌ No           |        ✅ Yes        |
| `sorted()`  |           ❌ No           |        ✅ Yes        |


| Operation             | New Object? | Modifies Existing Object? |
| --------------------- | :---------: | :-----------------------: |
| `append()`            |      ❌      |             ✅             |
| `extend()`            |      ❌      |             ✅             |
| `+=` (list)           |      ❌      |             ✅             |
| `list = list + [...]` |      ✅      |             ❌             |
| `copy()`              |      ✅      |             ❌             |


"""

