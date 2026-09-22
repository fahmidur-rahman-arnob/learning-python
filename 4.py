'''
for loops = execute a block of code a fixed number of times. you can iterate over a range, string, sequence, etc.

'''
#basic syntax inside range the second number is exclusive that's why you need 11 to count till 10. also counting starts at 0 I guess.
# for x in range(1, 11):
#     print(f"our number is {x}")

#counting backwords;
#for x in reversed(range(1, 11)):#reversed function does what it says it reverse stuffs... we are going from range 1 to range 10... but inside reverse function the ranges reversed ... we're going from 10 to 1. and when escape the loop we're printing bye.
    #print(f"Backwards {x}")
#print("Bye!")

#there's an additional parameter of range function.. lets say in this range(1, 11) function you want to count every 2 step then you'll add range(1, 11, 2) with this the python enterpreter will understand that you want every 2nd value
# for x in range(1, 11, 2):
#     print(f"Every 2nd is {x}")
# print("bye")
#reversed using 2nd step syntax to get more familiar;
# for x in reversed(range(1, 11, 2)):
#     print(f"Reversed 2nd Step {x}")
# print("bye")

#the range() isn't the only thing you can iterate over... you can also iterate over a string;
#example:
#credit_card = "1234-5678-9012-3456"
#for x in credit_card:
    #print(f"{x}",end="") #The end="" argument tells Python to not add a newline character (\n) at the end of a print() statement.

#break & continue;
#example - suppose we're going to count till 20, and let's consider 13 an unlucky number, and inside loop when your counter came accross 13 we'll skip that and iterate over that using continue 
#for x in range(1, 21):
    #if x == 13:
        #continue #this tells to skip 13, 13 will not be printed
    #if x == 13:
        #break # this will stop the program at 12, because when counter finds 13 it will stop the program and wont print 13 
    #else : 
        #print(x)
#print("bye!")

#nested loop;
#for x in range(3):#this code will run 3 times 
    #for y in range(1, 10):
        #print(y, end="")
    #if x < 2 :
        #print("-", end="")#this prints the dash after the first sequence or you can say it like this .. after x runs first time only then the dash will printed.

#Example (practice) - we'll print a rectangle .. we'll ask the user how many rows & columns this rectangle will have .. and then we will print that using some symbols...
# rows = int(input("Enter how many rows you want - "))
# columns = int(input("Enter how many columns you want - "))
# symbol = input("Enter a symbol to use to make the rectangle:  ")
# for x in range(rows):#changed in range(3) to in range(rows)
#     for y in range(columns):#change in range(1, 11) to in range(columns)
#         print(symbol, end="")
#     print()


# ----------- Collections -----------
'''
collections = single "variable" used to store multiple values.
    1. lists = [] -> ordered and changeable, duplicates OK.
    2. set = {} -> unordered and immutable, but Add/Remove OK, NO duplicates.
    3. tuple = () -> ordered and unchangeable, duplicates are OK but comparatively FASTER

'''

#lists -> the first element(apple) has an index of 0, just like strings 
fruits = ["apple", "orange", "banana", "coconut"]
#print(fruits[-1:])#prints the last one
#print(fruits[::2])#every 2nd element from index 0
#print(fruits[::-1])#from last to first
#print(fruits[0:])#from first to last
#for fruit in fruits: #mane holo...fruits er list er moddhe theke fruit..mane singular...for fruit in fruits print fruit... 
    #print(f"{fruit},", end=" ")

#to list the different methods that are available to a collection you can use dir() function
# print(dir(fruits))
# print(help(fruits))
#if you want the length of how many elements are within the collection there's the len() method
# print(len(fruits))
#using the in operator we can see if a value is on the collection or not 

#print("apple" in fruits)#will return in boolean, with other collections as well.

#lists are changeable.. so we can change the values even after we declare our list...for ex. I want to change value at index[0] from apple to guava
#fruits[0] = "guava"
#print(fruits[0:])#see the value got changed
#we can also add a value in the list after we declare it

#fruits[0] = "guava"
#some of the methods of lists
#fruits.append("pineapple")#this adds pineapple at the end of the list.
#fruits.remove("apple")#apple will be removed;
#fruits.insert(0, "strawaberry")#using insert we can insert a value at a given index.first the index and then the value you want at that index.
#fruits.sort()#sort method will sort the list in alphabetical order.
#fruits.reverse()#these are not reversed in alphabetical order these are reverse based on the way we insert them.

#NOTE: if you want reverse in alphabetical order, you'll have to first sort and then reverse
#fruits.clear()#it'll clear the list
#print(fruits.index("orange"))#this will return the index of orange on the list.list starts from 0.


# print(fruits)