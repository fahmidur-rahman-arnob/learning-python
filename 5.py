'''
--------------- Sets in python ----------------
Set is a built-in Python data type used to store a collection of unique items.

    Stores only unique elements; duplicate values are automatically removed.

    Unordered collection, so elements do not have a fixed position and cannot be accessed using indexes.

    Supports fast search, insertion and deletion operations using hashing internally.



Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets*.
'''

#Set:
# fruits = {"apple", "orange", "banana", "coconut"}
# #print(dir(fruits))
# print(len(fruits))
# print(fruits)

#Tuple:
fruits = ("apple", "orange", "banana", "coconut")
#print(dir(fruits))
#print(len(fruits))
#print(fruits)
# thistuple1 = ("apple",)#this is a class<tuple>
# thistuple2 = ("apple") #this is a class<str>
# print(type(thistuple1))
# print(type(thistuple2))
print("apple" in fruits) #will return a boolean value