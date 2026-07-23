"""
✔ What is a Dictionary?
✔ Creating Dictionaries
✔ Key-Value Pairs
✔ Ordered Nature
✔ Mutable Nature
✔ Unique Keys
✔ Accessing Values
✔ get()
✔ Updating Values
✔ Adding New Keys
✔ Removing Keys
✔ Iteration
✔ len()
✔ Membership Operator
✔ Nested Dictionaries
✔ Common Interview Questions
✔ Quick Revision"""



#1. What is a Dictionary?

"""
A dictionary is an ordered, mutable collection of key-value pairs.
It stores data as key : value mappings.
Keys must be unique and hashable, while values can be of any data type.
Always close the dictionary with curly brackets and seperate the key : value pairs with , (comma).

"""

#2. Create a dictionary

# empty dictionary
dict = {}
print(type(dict))

# Dictionary with values in it 
dict1 ={1:2,2:4,'a':'a',(5,6):"Divya"}
print(type(dict1))
print("Dictionary : ",dict1)



#3. Key - value pair 

"""Dictionary consists of a key - value pair 
   Left side denotes a key which should be unique and hashable & right side denotes a value which can be of any data type   
   We can fetch keys by dictionary.keys() and values by dictionary.values()"""

dict_1 = {'a':2,'r':4,1:"divya",3.5:"a"}
print("Dictionary keys : ", dict_1.keys())    #keys 
print("Dictionary values : ",dict_1.values()) #values
print("Dictionary key-value pairs : ",dict_1.items()) #items


#4. Ordered Nature 
dict_1 = {'a':2,'r':4,1:"divya",3.5:"a"}
print(dict_1[1])    #fetch dictionary elemnts with the key present in the dictionary

#5. Mutable Nature
#Dictionary is mutable in nature ,we can change,add ,remove key - value pair from the dictionary 


# change the value:
dict_1['a'] =10
print("Dictionary after modification : ",dict_1)

#add pair 
dict_1['b'] = "Diu"
print("Dictionary after adding the pair  : ",dict_1)


#remove the pair 
del(dict_1['r'])
print("Dictionary after deleting the pair  : ",dict_1)



#6.Unique Keys

#Dictionary with the duplicate keys 

v = {1:'a',1:'r',1:6}   # this will not give an error ,it will overwrite with the updated value
print(v)  #o/p = {1,6}

print("Keys present in the dictionary  : " ,v.keys())    #o/p = 1



#7.Accessing Values

sample = {'a':1,1:'a', 3.4:"divya"}
print("Accessing the dictionary : " ,sample[3.4])



#8.get()

print(sample.get('a')) # get the value 


#9.Updating value:

dict_sample = {'a':56,'b':0}
dict_sample['a'] =10
print("Dictionary after modification : ",dict_sample)

#10.Adding New Keys
dict_sample['c'] = "Diu"
print("Dictionary after adding the key : ",dict_sample)


#11.Removing Keys
del(dict_1['b'])
print("Dictionary after deleting the key : ",dict_sample)


#12.Iteration

# Default iteration returns keys

sample = {1:3,'a':"divya",1.4:"d"}
print("\nDefault Iteration : ")
for key in sample :
       print(key ,end =" ")


# Iteration using keys()
print("\nIteration using keys() : ")
for k in sample.keys():
       print(k,end=" ")

# Iteration using values()
print("\nIteration using values() : ")
for val in sample.values():
       print(val,end = " ")

# Iteration using items()

#---1----
print("\nIteration using items() : ")
for val in sample.items():
       print(val,end = " ")

#---2----
print("\nIteration using items() : ")
for key,val in sample.items():
       print(key," : ",val)



#13.Common Interview Questions

"""
Q1. What is returned when we iterate over a dictionary?

Answer: Keys.

Example:

for x in dictionary:

returns keys.

----------------------------------------

Q2. Difference between keys(), values() and items()?

keys() : Returns all keys.

values() : Returns all values.

items() : Returns (key, value) pairs.

----------------------------------------

Q3. What does items() return?

Answer: A view object containing tuples.

Example

('name', 'Divya')

('age', 23)

----------------------------------------

Q4. Does dictionary iteration preserve order?

Answer : Yes.

Python 3.7+ preserves insertion order.

----------------------------------------

Q5. Time Complexity of Dictionary Iteration?

Answer : O(n)

because every key-value pair is visited once."""


#14.Quick Revision 

"""
✔ for key in dict → keys

✔ dict.keys() → all keys

✔ dict.values() → all values

✔ dict.items() → key-value tuples

✔ enumerate(dict.items()) → index + key + value

✔ 'in' checks keys by default

✔ Dictionary iteration → O(n)

"""
    

