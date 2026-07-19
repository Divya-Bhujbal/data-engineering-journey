"""
=========================================================
Topic        : String Slicing
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered
--------------
✔ What is Slicing?
✔ Slice Syntax
✔ Start Index
✔ Stop Index
✔ Step
✔ Positive Slicing
✔ Negative Slicing
✔ Reverse String
✔ Copying Strings
✔ Out-of-Range Slicing
✔ Common Interview Questions
✔ Coding Challenges
✔ Quick Revision

=========================================================
"""

# =====================================================
# 1. What is Slicing?
# =====================================================

"""
String slicing is used to extract a portion (substring) from a string.
Unlike indexing, slicing returns a NEW string.
The original string remains unchanged because strings are  immutable.

"""

name = "Divya"

print(name[0:3])        # Div

# =====================================================
# 2. Slice Syntax
# =====================================================

"""
General Syntax

string[start : stop : step]

start -> Inclusive

stop -> Exclusive

step -> Number of characters to skip

Default values

start = 0
stop = len(string)
step = 1
"""

language = "Python"

print(language[0:4])        # Pyth

# =====================================================
# 3. Start Index
# =====================================================

"""
If the start index is omitted, Python starts from index 0.
"""

print(language[:2])         # Py

print(language[:4])         # Pyth

print(language[:])          # Python

# =====================================================
# 4. Stop Index
# =====================================================

"""
If stop index is omitted, Python slices till the end.
"""

print(language[2:])         # thon

print(language[4:])         # on

# =====================================================
# 5. Step
# =====================================================

"""
Step decides how many positions Python moves after selecting each character.

Default step = 1
"""

print(language[::1])        # Python

print(language[::2])        # Pto

print(language[1::2])       # yhn

print(language[::3])        # Ph

# =====================================================
# 6. Positive Slicing
# =====================================================

word = "Programming"

print(word[0:7])            # Program

print(word[3:8])            # gramm

print(word[4:11])           # ramming

# =====================================================
# 7. Negative Slicing
# =====================================================

"""
Negative indexing starts from the end.-1 represents the last character.
"""

print(word[-4:])            # ming

print(word[:-4])            # Programm

print(word[-7:-2])          # ammin

# =====================================================
# 8. Reverse String
# =====================================================

"""
Negative step reverses the direction.
"""

language = "Python"

print(language[::-1])       # nohtyP

print(language[::-2])       # nhy

print(language[::-3])       # nt

# =====================================================
# 9. Copying a String
# =====================================================

"""
Slicing creates a new string.
Strings are immutable.
"""

text = "Python"

copy_text = text[:]

print(copy_text)

print(copy_text == text)

print(copy_text is text)

# =====================================================
# 10. Out-of-Range Slicing
# =====================================================

"""
Unlike indexing,
slicing NEVER raises IndexError.
Python automatically adjusts the indices.
"""

language = "Python"

print(language[0:100])

print(language[100:200])

print(language[-100:4])

# =====================================================
# 11. Empty Slice
# =====================================================

"""
If start index is greater than stop index (with positive step),
Python returns an empty string.
"""

print(language[4:2])

print(language[2:2])

# =====================================================
# 12. Common Interview Questions
# =====================================================

"""
Q1.

Difference between indexing and slicing?

Indexing : Returns one character.

Slicing : Returns a new string.
"""

"""
Q2.

Does slicing modify the original string?

Answer
No.
Strings are immutable. Slicing always creates a new string.
"""

"""
Q3.What are the default values?

start = 0
stop = len(string)
step = 1
"""

"""
Q4.What happens if the indices are out of range?

Answer
Python does NOT raise IndexError.
It simply returns the available characters.
"""

"""
Q5.Time Complexity of slicing?

Answer
O(k)
where k = number of copied characters.
"""

# =====================================================
# 13. Coding Challenges
# =====================================================

"""
Predict the Output
"""

word = "Database"

print(word[2:6])

print(word[:5])

print(word[5:])

print(word[::2])

print(word[::-1])

print()

language = "Python"

print(language[-4:-1])

print(language[:-2])

print(language[1:6:2])

print(language[::])

print(language[::-1])

print(language[3:1])

print(language[3:1:-1])

# =====================================================
# 14. Quick Revision
# =====================================================

"""
✔ Syntax

string[start : stop : step]

✔ start -> Inclusive

✔ stop -> Exclusive

✔ step -> Number of characters to skip

✔ Default start = 0

✔ Default stop = len(string)

✔ Default step = 1

✔ Negative step reverses the string.

✔ Slicing returns a NEW string.

✔ Strings remain immutable.

✔ Slicing never raises IndexError.

✔ Empty slice returns ''.

✔ Time Complexity = O(k)
"""