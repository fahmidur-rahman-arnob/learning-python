#logical operators == evaluate multiple conditions(or, and, not)
#                  or = at least one condition must be True;
#                  and = both conditions must be True;
#                  not = inverts the condition (not False, not True)

'''GFG NOTE: Logical operators are used to combine or modify conditions and return 
a Boolean result (True or False). They are commonly used in conditional statements 
to control the flow of a program based on multiple logical conditions.

#Example: 
# a, b, c = True, False, True
# if a and c : 
#     print("Both A and C are true (AND Condition).")
# if b or c :
#     print("Either B or C are true (OR Condition).")
# if not b : 
#     print("b is False (NOT condition).")
 
# output:
# Both a and c are True (AND condition).
# Either b or c is True (OR condition).
# b is False (NOT condition).

Explanation:
    # a and c returns True because both values are True.
    # b or c returns True because at least one value is True.
    # not b reverses False to True, so the condition executes.

AND -> and	Returns True if both the operands are true -> x and y -> x>7 and x>10 
OR -> or	Returns True if either of the operands is true -> x or y -> x<7 or x>15
NOT -> not	Returns True if the operand is false -> not x -> not(x>7 and x> 10)


Order of Precedence of Logical Operators: 
And operator has higher precedence than Or, so AND is evaluated first.

'''

#Example - 1 (Below Program Shows how the AND operator works)
# a = 10
# b = 10
# c = 10

# if a > 0 and b > 0 : 
#     print("Numbers are greater than 0.")
# if a > 0 and b > 0 and c > 0 : 
#     print("Numbers are greater than 0.")
# else : 
#     print("Atleast one number is not greater than 0.")

#Example - 2 (The code checks if all variables a, b and c evaluate to True, printing a message accordingly.)
# a = 10
# b = 12
# c = 0

# if a and b and c : 
#     print(f"All numbers {a}, {b}, and {c} have boolean value as True.")
# else : 
#     print("At least one number has boolean value as False.")

# Note: If the first expression is evaluated to be false while using the AND operator, 
# then the further expressions are not evaluated.

# Example - 3 (A updated version of ex. - 2, where the user inputs a number and then the program checks if all the variable evaluates to True, printing a message accordingly.)
# a = int(input("Enter a Number - "))
# b = int(input("Enter a Second Number - "))
# c = int(input("Enter a Third Number - "))

# if a and b and c :
#     print(f"All numbers {a}, {b}, and {c} have boolean value as True.")
# else : 
#     print("At least one number has boolean value as False.")



# Example - 1 (where the condition becomes true if at least one of the given expressions evaluates to True.) -> THE OR OPERATOR 
# a = 10
# b = -10
# c = 0

# if a > 0 or b > 0 : 
#     print("Either of the number is greater than 0.")
# else : 
#     print("No Number is greater than 0.")

# if b > 0 or c > 0 : 
#     print("Either of the number is greater than 0.")
# else : 
#     print("No Number is greater than 0.")

# Example - 2 (The code checks if any of the variables a, b or c has a boolean value as True; if so, it prints "At Least one number has boolean value as True.")
# a = 10
# b = 12
# c = 0

# if a or b or c : 
#     print("At least one number has boolean value as True.")
# else : 
#     print("All the numbers have boolean value as False.")

# Example - 1 (Below code checks if a is divisible by either 3 or 5, otherwise, it prints a message indicating that it is not.) NOT OPERATOR
# a = 10
# if not a : 
#     print("Boolean value of a is True.")
# if not (a % 3 == 0 or a % 5 == 0) : 
#     print("10 is not divisible by either 3 or 5.")
# else :
#     print("10 is divisible by either 3 or 5.")


'''
#Conditional Expressions - A one line shortcut for the 
if-else statement(Ternary Operator)
print or assign one of the two values on a condition
X if condition else Y

'''
# num = 5
# num = int(input("Enter a number - "))
# print("positive" if num > 0 else "Negative")
# # print("Positive" ? num >= 0 : "Negative") #doesn't work, WHY?

# result = "The Number is EVEN" if num % 2 == 0 else "The Number is ODD"
# print(result)

# String Methods in Python

#name = input("Enter Your Full Name - ")
#result = len(name) #returns the length of a string(counts spaces too)
#result = name.find("F") #finds the first occurance of a string
#result = name.rfind("0") #finds the last occurance of a string, r means reverse;
#result = name.capitalize() #Converts the first character of the string to uppercase and the remaining characters to lowercase.
#result = name.lower() #converts all uppercase to lowercase
#result = name.upper() #converts all lowercase to uppercase
#result = name.replace("Arnob", "Anika")
# if name.find("Arnob") : #you can check whether "ARNOB" all the chars are in the given string or not then you can changge them by using the replace func. find returns the location of those chars and then replace them.
#     result = name.replace("Arnob", "Anika")
#     print(f"The length of your name is {result}")
# else :
#     print("Not Found")
#print("-".join(name))
#result = name.count("a")
#result = name.strip(" ") #removes the first and the last space from string
# print(f"The length of your name is {result}")
# print(result)