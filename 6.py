'''
Python provides flexible data structures such as lists, which can be used to represent 1D and 2D arrays. A 2D list in Python is essentially a list of lists, commonly used to store data in a table-like format with rows and columns.

basically a 2D list is a list of lists...

'''

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turky"]

#another way of declaring 2D list...but the above approach is more suitable for me ... but the below approach is more readable...this a list of list by the way
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turky"]]
#print(groceries[0]) #groceries[0] means to print the 0th row which is the fruits list. but if I print groceries[0][0] it'll print apple...so basically in 2D lists all the other lists are considered as rows and the values inside those lists are considered as columns...
# print(groceries[0][0])
# print(groceries[1][0])
# print(groceries[2][0])

#if you ever have to iterate over a 2D lists..you're gonna need a nested loop...

#for collection in groceries : 
    #print("rows - ",collection) # this will only iterate over the rows.. if want the columns as well then you're gonna need another loop...
    #for food in collection :
        #print("columns - ", food, end = " ") #this will give us all the columns in the rows

    #print()

#we can also create a list of tuples...like below
# groceries = [("apple", "orange", "banana", "coconut"),
#              ("celery", "carrots", "potatoes"), 
#              ("chicken", "fish", "turky")]


#you can also make a tuple of tuple(2D tuple)\
# groceries = (("apple", "orange", "banana", "coconut"),
#              ("celery", "carrots", "potatoes"), 
#              ("chicken", "fish", "turky"))


#you can also make tuple made up of sets 
# groceries = [{"apple", "orange", "banana", "coconut"},
#              {"celery", "carrots", "potatoes"}, 
#              {"chicken", "fish", "turky"}]

# for collection in groceries : 
#     #print(collection)
#     for food in collection :
#         print(food, end=" ")
#     print()


#example - let's make a 2D keypad 
# num_pad = ((1, 2, 3), 
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))
# for row in num_pad:
#     #print("row - ",row)
#     for num in row : 
#         print(num, end=" ")
#     print()



'''
Dictionary = a collection of {key:value} pairs, 
             ordered and changeable. NO DUPLICATES.
'''
# capitals = {
#     "USA" : "Washington D.C.",
#     "Bangladesh" : "Dhaka",
#     "India" : "New Delhi",
#     "China" : "Beijing",
#     "Russia" : "Moscow"
# }
# print(dir(capitals))
# print(help(capitals))

#some methods of dict.
#print(capitals.get("USA")) # The value associated with this key will be printed ... If I change the key then the value associated with that key will be printed...basically you've to pass a key to get() method in order to get the value; if python doesn't find a key than it'll return None, we can use it with if statement;
# if capitals.get("Russia"):
#     print("That capital exists.")
# else:
#     print("That capital doesn't exists.")

#to update our dict.
# capitals.update({"Germany" : "Berlin"})
# print(capitals)

#to remove all key-value pairs in a dict. use clear()
# capitals.clear()
# print(capitals)

#copy() returns a shallow copy of the dictionary
# new_capitals = capitals.copy()
# print(new_capitals)

#items() will all key-value pairs as tuples
# print(list(capitals.items()))
# print(capitals.items())

#keys() this will return all key's in a dict.
#print(list(capitals.keys()))
#print(capitals.keys())

#values() this will return all values in a dict.
#print(list(capitals.values()))
#print(capitals.values())

#pop() will remove a specified key and returns it's value
# print(capitals.pop("USA"))
# print(capitals)

#popitem() removes and returns the inserted key-value pair
# print(capitals.popitem())
# print(capitals)