"""Topic        : Tuple Methods
Difficulty   : Beginner
Author       : Divya Bhujbal

Topics Covered

✔ count()
✔ index()
✔ Concatenation (+)
✔ Repetition (*)
✔ max()
✔ min()
✔ sum()
✔ sorted()
✔ Common Interview Questions
✔ Quick Revision

=========================================================
"""

# Tuple Methods

"""
Tuples are immutable.

Therefore, Python provides only two built-in methods:

1. count()
2. index()

Other operations like max(), min(), sorted(), etc.
are built-in functions, not tuple methods.
"""


#1. count()

a = ('a',1,2.3,'A','a')
print("Count of a : ",a.count('a'))


#2.index()      ---> Returns the index of the first occurrence of a value.Raises ValueError if the value is not present.

print("Index ", a.index('A'))


#3. Tuple Concatenation

a = (1,'m',6.70)
b = ('divya',110)
print("Tuple concatenation ",a+b)


#4. Tuple Repetition
print("Tuple Repetition ",a*2)



#5.max(), min(), sum()

d = (2,3,4,6,1322)
print("max ",max(d))
print("min ",min(d))
print("sum ",sum(d))


#6. ✔ sorted()     ->sorted() returns a NEW LIST.It does NOT return a tuple.
d = (123,2,3,4,6,1322)
print(type(sorted(d)))
print(d)


# ---------------------------------------------------------
# Common Interview Questions
# ---------------------------------------------------------

"""
Q1. How many methods does a tuple have?

Answer

Only two:

1. count()
2. index()

--------------------------------------------------

Q2. Why are there so few tuple methods?

Answer

Because tuples are immutable.

They cannot be modified after creation.

--------------------------------------------------

Q3. Does sorted() modify the tuple?

Answer

No.

It returns a NEW list.

--------------------------------------------------

Q4. Can we sort a tuple?

Answer

Yes.

Use sorted().

If a tuple is required:

tuple(sorted(tuple_name))

--------------------------------------------------

Q5. Difference between sort() and sorted()?

sort()

• List method
• Modifies original list
• Returns None

sorted()

• Built-in function
• Returns a new sorted list
• Works on any iterable

"""

# ---------------------------------------------------------
# Quick Revision
# ---------------------------------------------------------

"""

✔ Tuples are immutable.

✔ Only two tuple methods:
   count()
   index()

✔ + creates a new tuple.

✔ * repeats the tuple.

✔ max() returns largest value.

✔ min() returns smallest value.

✔ sum() returns total.

✔ sorted() returns a LIST.

✔ tuple(sorted(tuple_name))
   converts it back to a tuple.

"""
"""
Most asked interview question 


a = (1, 2, [3, 4])

a[2].append(5)

print(a)

Output:

(1, 2, [3, 4, 5])

Why?

The tuple itself is immutable (you can't replace its elements), but it can contain mutable objects like lists. 
Modifying the list does not modify the tuple's structure.

"""