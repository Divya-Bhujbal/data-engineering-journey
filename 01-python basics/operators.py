"""
=========================================================
Topic        : Operators
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered
--------------
✔ Arithmetic Operators
✔ Comparison Operators
✔ Assignment Operators
✔ Logical Operators
✔ Identity Operators
✔ Membership Operators
✔ Bitwise Operators
✔ Operator Precedence
✔ Common Interview Questions

=========================================================
"""

# =====================================================
# 1. Arithmetic Operators
# =====================================================

"""
Arithmetic Operators

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponentiation
"""

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)    
print("Modulus:", a % b)
print("Power:", a ** b)

# =====================================================
# 2. Comparison Operators
# =====================================================

"""
Comparison Operators

==
!=
>
<
>=
<=

Returns True or False.
"""

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# =====================================================
# 3. Assignment Operators
# =====================================================

"""
Assignment Operators

=
+=
-=
*=
/=
//=
%=
**=
"""

num = 10

num += 5
print(num)

num *= 2
print(num)

num -= 4
print(num)

# =====================================================
# 4. Logical Operators
# =====================================================

"""
Logical Operators

and
or
not
"""

a = True
b = False

print(a and b)
print(a or b)
print(not a)

# =====================================================
# 5. Identity Operators
# =====================================================

"""
Identity Operators

is
is not

Checks whether two variables refer
to the same object.
"""

list1 = [1, 2]
list2 = list1
list3 = [1, 2]

print("list1 is list2 " ,list1 is list2)
print("list1 is list3" , list1 is list3)

print("list1 == list3",list1 == list3)

# =====================================================
# 6. Membership Operators
# =====================================================

"""
Membership Operators

in
not in
"""

name = "Divya"

print("D" in name)
print("z" in name)

numbers = [1, 2, 3]

print(2 in numbers)
print(10 not in numbers)

# =====================================================
# 7. Bitwise Operators
# =====================================================

"""
Bitwise Operators

&
|
^
~
<<
>>

Used mostly in systems programming.
Rarely used in Data Engineering,
but good to know for interviews.
"""

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

# =====================================================
# 8. Operator Precedence
# =====================================================

"""
Highest
|
|
|

()
**
+x  -x
* / // %
+ -
Comparison
not
and
or

|
|
|
Lowest
"""

print(2 + 3 * 4)
print((2 + 3) * 4)

# =====================================================
# 9. Common Interview Questions
# =====================================================

"""
Q1. Difference between / and // ?

/  -  Returns float.

// - Returns floor value.
"""

print(10 / 3)
print(10 // 3)

"""
Q2. Difference between == and is ?

==    -    Compares values.

is    - Compares object identity.
"""

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)

"""
Q3. Difference between & and and ?

&

Bitwise operator.

and

Logical operator.
"""

print(1 & 3)
print(True and False)

# =====================================================
# 10. Coding Challenges
# =====================================================

"""
Predict the output.
"""

print(10 + 5 * 2)
print((10 + 5) * 2)

print()

a = [1, 2]
b = a

print(a is b)
print(a == b)

print()

x = 10

x += 5

print(x)

# =====================================================
# 11. Quick Revision
# =====================================================

"""
Quick Revision

Arithmetic
----------
+  -  *  /  //  %  **

Comparison
----------
==  !=  >  <  >=  <=

Assignment
----------
=  +=  -=  *=  /=

Logical
-------
and
or
not

Identity
--------
is
is not

Membership
----------
in
not in

Bitwise
-------
&
|
^
~
<<
>>

Interview Tips
--------------
✔ == compares values.

✔ is compares object identity.

✔ / returns float.

✔ // returns floor division.

✔ and/or are logical operators.

✔ &, | are bitwise operators.
"""