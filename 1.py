#print('hello world')

#these are string variable
#first_name = 'Fahmidur'
#middle_name = 'Rahman'
#last_name = 'Arnob'
#print(f"hello {first_name} {middle_name} {last_name}")


#these are int variables
#your_age = 25
#quantity = 3
#people = 30
#print(f"your age is {your_age} and you're buying {quantity} items for {people} peoples.")

#these are float variables
#price = 10.99
#print(f"the products you bought for 30 peoples costs ${price}")

#these are boolean variables
# is_tasty = True
# is_tasty_2 = False
# print(f"The foods you bought are really tasty. is it {is_tasty} or {is_tasty_2}. ")

# is_student = True
# if is_student:
#     print("you can go.")
# else: 
#     print("you don't have access.")

# for_sale = True
# if for_sale:
#     print("price is $10.87.")
# else:
#     print("not for sale.")

# is_online = input("online or not: (yes/no)").lower().strip() in ('y', 'yes')
'''
strip():
    is a function that removes all leading and trailing whitespace from a string.
Whitespace includes spaces, tabs (\t), and newlines (\n).
It does not remove spaces in the middle of the string.

examples:
1. "  hello  ".strip()"hello"Removes spaces from both ends.
2. "hello world".strip()"hello world"Keeps the middle space untouched.
3. "\t\n yes \n".strip()"yes"Removes tabs and newline breaks.

code:(got it from google -- keeping it here for ref.)
    # Without .strip(), if the user types "yes ", this evaluates to False
    is_valid = "yes " in ('yes', 'y')  # Result: False

    # With .strip(), the accidental space is removed first
    is_valid = "yes ".strip() in ('yes', 'y')  # Result: True

in keyword:
    In Python, in ('y', 'yes') checks if the user's input matches any of the values inside that collection.
It is a shorthand way of saying: "Is the input equal to 'y' OR is it equal to 'yes'?"

Breaking It Down:
    1. ('y', 'yes') is a tuple (an unchangeable list) containing two valid options.
    2. in is a Python keyword that searches the tuple. 
    It returns True if a match is found, and False if it isn't.


# The long way ❌
if user_input == 'y' or user_input == 'yes':

# The Pythonic way  
if user_input in ('y', 'yes'):

examples:
    1. "yes" Is "yes" inside ('y', 'yes')? True
    2. "y" Is "y" inside ('y', 'yes')? True
    3. "no" Is "no" inside ('y', 'yes')? False
    4. "maybe" Is "maybe" inside ('y', 'yes')? False


also if you want to take an int as an input then you've got use int(input()) because naturally 
the input() func returns an string
'''
# if is_online:
#     print("Message sent.")
# else: 
#     print("Message not sent.")

# passed = input("did you passed the exam? (yes/no): ").lower().strip() in ('y', 'yes')
# if passed:
#     print("Congratulations! You've Passed The Exam.")
# else:
#     print("Shame on you.")

# married = input("Are you married? (yes/no): ").lower().strip() in ('y', 'yes')
# if married:
#     print("What is your wife's name?")
# else:
#     print("Get married")
# is_int = int(input())
#is_int = input() #takes an input from the user
#if is_int.isdigit(): #python looks at the text the user gave and asks that if the str contains numb. from 0-9
    #print("True") #this line only runs if the isdigit() func returns true, otherwise python jumps to else
    #actual_number = int(is_int) #Because the previous check proved the text contains only digits, it is now perfectly safe to convert the text string (like "25") into an actual mathematical integer (25)
#else: 
    #print("False") #the fallback plan

# married = input()
# if married.isdigit():
#     print("this will always returns false/no because the user will only input yes or no, which are str's. but yes")
#     actual_numbs = int(married)
# else:
#     print("this will always returns false/no because the user will only input yes or no, which are str's. but no")


#Typecasting: is the process of converting one data-type to another data-type.
#str(), int(), float(), bool()

# name = 'Fahmidur'
# age = 25
# got_how_much_money = 12.34
# married = True
# got_child = False

# print(type(name))
# print(type(age))
# print(type(got_how_much_money))
# print(type(married))
# print(type(got_child))

# got_how_much_money = int(got_how_much_money)

# print(f"after type-casting {got_how_much_money}")



