'''indexing = accessing elements of a sequence using []
(indexing operator) [start : end : step]


'''
#credit_numb = "1234-5678-9012-3456"
#print(credit_numb[2]) #this line is basically "print credit card number at index 0."
#if we want first 4 digits of any string then 
#print(credit_numb[0:4]) #this line is basically "print credit card number at index 0 to 3" the starting index is inclusive and the ending index is exclusive.

#and also let's say I want to print every index after the index of 4/5 then I dont need put an ending index.then the syntex would be print(credit_numb[5:]) putting that colon is enough for python to understand that I need everything after 5th index.
#print(credit_numb[5:])

#also if you need the last number of the string then just put -1 in the [].
#print(credit_numb[-1])

# print(credit_numb[::2]) #this will print every second number within the string.
#print(credit_numb[::2]) #if we change the number to 3, we would get every third charac. of the array.
# print(credit_numb[::3])

# Practical Example : let's create a program to get the last 3/4 digits of a credit card number;


# credit_numb = "1234-5678-9012-3456"
#last_digits = credit_numb[-4:] #starts at -4 and python will assume we need rest of the numbers.
#print(f"the last 4 digits of your credit card is - XXXX-XXXX-XXXX-{last_digits}")

# another program : let's reverse the characters of the string
#credit_numb = "1234-5678-9012-3456"
#reversed_numbs = credit_numb[::-1] #negative 1 will reverse the string...it'll print from the last index of the string to the first index.
# print(f"reversed string is - {reversed_numbs}")

#---------------- While loops ---------------
#name = input("Enter Your Name: ")

# if name == "":
#     print("You did not enter your name.")
# else:
#     print(f"Hello {name}.") #if you want to continue asking for a name ... in case of a login box or some case where I need the users information then looping until user gives info. while loop is efficient i guess. I can loop this if-else
# name = input("Enter Your Name: ")
# while name == "": #while this condition is true, execute the below code.
#     print("You did not enter your name.")
#     name = input("Enter Your Name: ")


# print(f"Hello There {name}.")


# you always need an exit strategy to avoid infinite looping.. 

#infinite loop 
# name = input("Enter Your Name - ")
# while name =="":
#     print("You did not enter your name.")

# print(f"Hello There {name}.")

#correct way:
# age = int(input("Enter Your Age - "))
# while age < 0 :
#     print("Age can't be negative.")
#     age = int(input("Enter Your Age - "))
# print(f"You Are {age} years old.")

# an example - we will ask a user enter his fav. food and press when he wants to exit the program.

# food_item = input("Enter a food you like - (q to quit)")

# while not food_item == 'q':
#     print(f"you like {food_item}")
#     food_item = input("Enter Another Food You Like - (q to quit)")
# print("bye")

# another example - we will ask a user to enter a number between 1 to 10 and q to quit the program.
# num = int(input("Enter a number between 1 to 10 - (q to quit)"))

# while num < 1 or num > 10 : 
#     print(f"{num} is not valid. Please enter a correct num.")
#     num = int(input("Enter another number between 1 to 10 - (q to quit)"))
# print(f"Your Num is - {num}")


