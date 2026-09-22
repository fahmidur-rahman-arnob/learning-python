#challenge - 8;
# username = input("Enter Your Username - ")
# password = input("Enter Your Password - ")

# if username.strip().lower() == 'admin' and password == '1234' :
#     print("Login Successful.")
# else :
#     print("Invalid UserName or Password.")

# Challenge - 9;
# number = int(input("Enter a number - "))
# if number > 0 : 
#     print("Positive.")
# else :
#     print("Negative.")

# print("Even" if number % 2 == 0 else "Odd")

#Challenge - 10;
# password = input("Enter Your Password - ")

# has_whitespace = password != password.strip()
# has_spacial_char = "@" in password or "#" in password or "$" in password

# if len(password) < 8 :
#     print("Invalid.")
# elif has_whitespace :
#     print("Invalid")
# elif not has_spacial_char : #using not make sure that the input string doesnot has those 3 chars in the string and returns boolean False..hence program prints Invalid.
#     print("Invalid.")
# else :
#     print("valid.")


#Challenge - 11;
#a = 10
#b = 0
#c = -5

#if a and b:
    #print("A") #doesn't print this because they're not the same value

#if a or b:
    #print("B") #prints because only one is true, because a is greater than 0

#if not b:
    #print("C") # C print korche karon ekhane False returns korche..QUESTION why is it returning false?need answer.

#if b and c:
    #print("D") # both of them are negative that's why not printing

#if b or c:
    #print("E") # ekhane C direct negative and b neither negative or positive tai ekta direct negative integer such as -5 er comparison e program 0 ke positive vebe print koreche.


#Challenge - 12;
# x = -10
# y = 0
# z = 5

# print(bool(x))
# print(bool(y))
# print(bool(z))

# if x and y:
#     print("A") # x Truthy y falsy

# if x or y:
#     print("B") # truthy or falsy

# if not y:
#     print("C") # not falsy

# if y or z:
#     print("D") #falsy or truthy

# if not x:
#     print("E") # not truthy 