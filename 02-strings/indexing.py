"""
=========================================================
Topic        : String Indexing
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered
--------------
✔ What is a String?
✔ String Internals
✔ Strings are Immutable
✔ Positive Indexing
✔ Negative Indexing
✔ len()
✔ Empty String
✔ Accessing Characters
✔ Iterating over Strings
✔ enumerate()
✔ Common Interview Questions
✔ Quick Revision

=========================================================
"""

# =====================================================
# 1. What is a String?
# =====================================================

"""
A string is an immutable sequence of Unicode characters.

It is a built-in Python data type that supports:
1. Indexing
2. Slicing
3. Concatenation
4. Iteration
"""

name = "Divya"

print(type(name))


# =====================================================
# 2. String Internals
# =====================================================

"""
1. Strings are immutable.
2. Once created, they cannot be modified.
3. Any modification creates a new string object.
"""

my_name = "Divya"

print("Before Modification :", id(my_name))

my_name = "Bhujbal " + my_name

print("After Modification  :", id(my_name))

print(my_name)


# =====================================================
# 3. Positive Indexing
# =====================================================

"""
Positive Indexing

1. Positive indexing starts from 0.
2. The first character has index 0.
3. Index increases from left to right.
"""

my_name = "Divya "

print(my_name[0])      # D
print(my_name[1])      # i
print(my_name[2])      # v
print(my_name[3])      # y
print(my_name[4])      # a
print(my_name[5])      # Space


"""
Visual Representation

 D  i  v  y  a
 0  1  2  3  4
"""


# =====================================================
# 4. Negative Indexing
# =====================================================

"""
Negative Indexing

1. Negative indexing starts from the end of the string.
2. The last character has index -1.
3. Index decreases as we move towards the beginning.
"""

my_name = "Divya "

print(my_name[-1])     # Space
print(my_name[-2])     # a
print(my_name[-3])     # y
print(my_name[-4])     # v
print(my_name[-5])     # i
print(my_name[-6])     # D


"""
Visual Representation

 D  i  v  y  a
-6 -5 -4 -3 -2 -1
"""


# =====================================================
# 5. len()
# =====================================================

"""
len()

Returns the number of characters in a string.

Spaces are also counted as characters.
"""

text = "Di vya"

print(len(text))


# =====================================================
# 6. Empty String
# =====================================================

"""
An empty string has:

Length = 0

Boolean Value = False
"""

empty = ""

print(type(empty))
print(len(empty))
print(bool(empty))


# =====================================================
# 7. Accessing Characters
# =====================================================

"""
Characters can be accessed using indexing.

Valid Positive Index

0 to len(string)-1

Valid Negative Index

-len(string) to -1
"""

language = "Python"

print(language[0])      # P

print(language[3])      # h

print(language[-1])     # n

print(language[-3])     # h


# =====================================================
# 8. Iterating over a String
# =====================================================

"""
Strings are iterable.

We can iterate character by character.
"""

my_name = "Divya"

for character in my_name:
    print(character, end=" ")

print()


# =====================================================
# 9. enumerate()
# =====================================================

"""
enumerate()

Returns both:

1. Index
2. Character
"""

my_name = "Divya"

for index, character in enumerate(my_name):
    print(index, character)


# =====================================================
# 10. IndexError
# =====================================================

"""
Accessing an invalid index raises

IndexError
"""

language = "Python"

# Uncomment to see the error

# print(language[10])


# =====================================================
# 11. Common Interview Questions
# =====================================================

"""
Q1. Why does Python support negative indexing?

Answer

It allows easy access to characters
from the end of a sequence without
calculating the length.
"""

"""
Q2. Is string indexing O(1) or O(n)?

Answer

O(1)

Reason

Python can directly access a character
using its index.
"""

"""
Q3. Can we modify a character using indexing?

Example

language = "Python"

language[0] = "J"

Answer

No.

Output

TypeError:
'str' object does not support item assignment

Reason

Strings are immutable.
"""

"""
Q4. Is there a separate character data type in Python?

Answer

No.

'A'

is a string of length 1.
"""

print(type("A"))

print(len("A"))


"""
Q5. What happens if we access an index
greater than the string length?

Answer

Python raises

IndexError
"""

# print("Python"[100])


# =====================================================
# 12. Coding Challenges
# =====================================================

"""
Predict the Output
"""

word = "Database"

print(word[0])

print(word[-1])

print(word[4])

print(len(word))


print()

language = "Python"

print(language[0])

print(language[-2])

print(len(language))


# =====================================================
# 13. Quick Revision
# =====================================================

"""
✔ String is an immutable sequence of Unicode characters.

✔ String is an ordered sequence.

✔ Supports indexing, slicing, concatenation and iteration.

✔ Positive indexing starts from 0.

✔ Negative indexing starts from -1.

✔ len() returns the number of characters.

✔ Spaces are counted in len().

✔ Empty string has length 0.

✔ bool("") returns False.

✔ Valid Positive Index
0 to len(string)-1

✔ Valid Negative Index
-len(string) to -1

✔ String indexing complexity is O(1).

✔ Strings are immutable.

✔ Modifying a string creates a new object.

✔ Accessing an invalid index raises IndexError.

✔ Python has NO separate character data type.

'A' is a string of length 1.
"""