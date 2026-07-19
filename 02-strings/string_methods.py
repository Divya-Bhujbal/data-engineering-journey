"""
=========================================================
Topic        : String Methods
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered
--------------
✔ What are String Methods?
✔ Case Conversion Methods
✔ Searching Methods
✔ Modification Methods
✔ Splitting & Joining
✔ Checking Methods
✔ Interview Questions
✔ Coding Challenges
✔ Quick Revision

=========================================================
"""

# =====================================================
# 1. What are String Methods?
# =====================================================

"""
String methods are built-in functions associated with string objects that perform various operations on strings.

Since strings are immutable, most string methods return a NEW string instead of modifying the original string.

Some methods return integers or boolean values instead of strings.
"""

text = "python"

print(text.upper())
print(text)          # Original string remains unchanged


# =====================================================
# 2. Case Conversion Methods
# =====================================================

# -----------------------------------------------------
# upper()
# -----------------------------------------------------

"""
Converts all alphabetic characters to uppercase.
"""

name = "divya"

print(name.upper())      # DIVYA
print(name)

# -----------------------------------------------------
# lower()
# -----------------------------------------------------

"""
Converts all alphabetic characters to lowercase.
"""

name = "DIVYA"

print(name.lower())
print(name)

# -----------------------------------------------------
# title()
# -----------------------------------------------------

"""
Capitalizes the first letter of every word.
"""

sentence = "india is my COUNTRY"

print(sentence.title())

# -----------------------------------------------------
# capitalize()
# -----------------------------------------------------

"""
Capitalizes only the first character of the string.
"""

text = "python programming"

print("capitalize",text.capitalize())

# -----------------------------------------------------
# swapcase()
# -----------------------------------------------------

"""
Converts uppercase letters to lowercase and lowercase letters to uppercase.
"""

text = "Python Programming"

print("swapcase",text.swapcase())


# =====================================================
# 3. Searching Methods
# =====================================================

# -----------------------------------------------------
# find()
# -----------------------------------------------------

"""
Returns the first index of the substring.Returns -1 if not found.Case Sensitive.
"""

text = "I love Python"

print("Find text ",text.find("love"))

print("Find text ",text.find("Love"))

print("Find text ",text.find("Java"))

# -----------------------------------------------------
# index()
# -----------------------------------------------------

"""
Similar to find().
Difference- find() returns -1 & index() raises ValueError if substring is absent.
"""
text = "Python"

print("Index ",text.index("th"))

#uncomment to see a difference
#print("Index ",text.index("Java"))

# -----------------------------------------------------
# count()
# -----------------------------------------------------

"""
Returns the number of occurrences of a substring. Case sensitive.
"""

text = "apple apple mango Apple"

print("Text count ",text.count("apple"))

print(text.count("banana"))


# =====================================================
# 4. Modification Methods
# =====================================================

# -----------------------------------------------------
# replace()
# -----------------------------------------------------

"""
replace(old, new), Returns a new string.
"""

text = "I love cat"
new_text = text.replace("cat", "dog")
print("Replace new text ",new_text)
print("Replace original text ",text)

"""
replace(old, new, count) : Replaces only the specified number of occurrences.
"""

text = "cat cat cat"

print("Replace specific no of occurrence " ,text.replace("cat", "dog", 2))

# -----------------------------------------------------
# strip()
# -----------------------------------------------------

"""
Removes whitespaces from both ends.
"""

text = "   Pyt  hon   "

print("Strip",text.strip())

# -----------------------------------------------------
# lstrip()
# -----------------------------------------------------

"""
Removes whitespaces from the left side.
"""

print(text.lstrip())

# -----------------------------------------------------
# rstrip()
# -----------------------------------------------------

"""
Removes whitespaces from the right side.
"""

print(text.rstrip())

# =====================================================
# 5. Splitting & Joining
# =====================================================

# -----------------------------------------------------
# split()
# -----------------------------------------------------

"""
Splits a string into a list. Default split is based on a space.
"""

text = "Python SQL Spark"

print("Split ",text.split())

text = "apple,banana,mango"

print("Split by comma ",text.split(","))

# -----------------------------------------------------
# join()
# -----------------------------------------------------

"""
Joins elements of an iterable into a single string.
"""

subjects = ["Python", "SQL", "Spark"]
print("type of subjects " ,type(subjects))

print("Joined by space ", " ".join(subjects))

print("-".join(subjects))

print(",".join(subjects))


# =====================================================
# 6. Checking Methods
# =====================================================

# -----------------------------------------------------
# isalpha()
# -----------------------------------------------------

"""
Returns True if all characters are alphabets.
"""

print("Python".isalpha())

print("Python123".isalpha())

# -----------------------------------------------------
# isdigit()
# -----------------------------------------------------

"""
Returns True if all characters are digits.
"""

print("12345".isdigit())

print("123A".isdigit())

# -----------------------------------------------------
# isalnum()
# -----------------------------------------------------

"""
Returns True if every character is either alphabet or digit.
Spaces and special characters are not allowed.
"""

print("Python123".isalnum())

print("Python 123".isalnum())

print("Python@123".isalnum())

# -----------------------------------------------------
# isspace()
# -----------------------------------------------------

"""
Returns True if all characters are whitespaces.
"""

print("Isspace " ,"   ".isspace())

print("\t".isspace())   # \t blank tab space

print("\n".isspace())   # \n new line

print("Python".isspace())

# -----------------------------------------------------
# islower()
# -----------------------------------------------------

print("python".islower())

print("Python".islower())

# -----------------------------------------------------
# isupper()
# -----------------------------------------------------

print("PYTHON".isupper())

print("Python".isupper())

# -----------------------------------------------------
# istitle()
# -----------------------------------------------------

print("Python Programming".istitle())

print("python programming".istitle())

# -----------------------------------------------------
# startswith()
# -----------------------------------------------------

"""
Checks whether a string starts with the given prefix.Case sensitive.
"""

text = "Data Engineering"

print(text.startswith("Data"))

print(text.startswith("data"))

# -----------------------------------------------------
# endswith()
# -----------------------------------------------------

"""
Checks whether a string ends with the given suffix.
"""

print(text.endswith("Engineering"))

print(text.endswith("engineering"))


# =====================================================
# 7. Common Interview Questions
# =====================================================

"""
Q1.

Do string methods modify the original string?

Answer
No.
Strings are immutable.Most methods return a new string.
"""

"""
Q2.
Difference between
find() and index()?

find() - Returns -1

index() - Raises ValueError.
"""

"""
Q3.Difference between capitalize() and title()?

capitalize() - Only first character.

title() - First character of every word.
"""

"""
Q4.Difference between split() and join()?

split() - String → List
join() - List → String
"""

"""
Q5.Why does replace() return a new string?
Answer
Because strings are immutable.
"""


# =====================================================
# 8. Coding Challenges
# =====================================================

"""
Predict the Output
"""

text = "Python Programming"

print(text.upper())

print(text.lower())

print(text.title())

print(text.swapcase())

print(text.find("Program"))

print(text.count("m"))

print(text.startswith("Python"))

print(text.endswith("ing"))

print("123".isdigit())

print("Python123".isalnum())

print("Python".replace("P", "J"))

print("".join(["A", "B", "C"]))

print("A,B,C".split(","))


# =====================================================
# 9. Quick Revision
# =====================================================

"""
Case Conversion
---------------
upper()
lower()
title()
capitalize()
swapcase()

Searching
----------
find()
index()
count()

Modification
------------
replace()
strip()
lstrip()
rstrip()

Splitting & Joining
-------------------
split()
join()

Checking
---------
isalpha()
isdigit()
isalnum()
isspace()
islower()
isupper()
istitle()
startswith()
endswith()

Interview Points
----------------
✔ Strings are immutable.

✔ Most string methods return a NEW string.

✔ find() returns -1.

✔ index() raises ValueError.

✔ split() converts String → List.

✔ join() converts List → String.

✔ replace() returns a new string.

✔ startswith() and endswith() are case-sensitive.
"""