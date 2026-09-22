#challenge - 1;
# username = input("Enter Your Username - ")
# password = input("Enter Your Password - ")

# if "admin" in username and "1234" in password :
#     print("Login Successful.")
# else : 
#     print("Invalid Username or Password.")

#Challenge - 2;
# age = int(input("Enter Your Age - "))
# citizenship = input("Are You a Citizen?(yes/no) - ").lower().strip() in ('y', 'yes')
# if age >= 18 and citizenship :
#     print("Yes He's an Adult and He's a valid citizen.")
# else :
#     print("Either He's not adult or not a citizen.")

#challenge - 3;
#name = input("Enter Your Name - ")
# if name.find("Arnob") != -1 :
#     print("Arnob Found!")
# else : 
#     print("Arnob not found!")
# if "Arnob" in name : 
#     print("Arnob Found!")
# else : 
#     print("Arnob not found!")

#Challenge - 4;
# number = int(input("Enter a number - "))
# print("Positive and Odd" if number > 0 and number % 2 != 0 else "Negative and Odd")
# print("Positive and Even" if number > 0 and number % 2 == 0 else "Negative and Even") 
# if number > 0 and number % 2 == 0 :
#     print("Positive and Even")
# elif number > 0 and number % 2 != 0 :
#     print("Positive and Odd.")
# else : 
#     print("negative")

#Challenge - 5;
# string = input("Enter Your String - ")
# total_len = len(string)
# Num_of_a = string.count('a')
# sen_upp = string.upper()
# sen_lower = string.lower()
# occ_of_a = string.find('a')
# last_occ_of_a = string.rfind('a')
# print(f"All the answers are {total_len}, {Num_of_a}, {sen_upp}, {sen_lower}, {occ_of_a}, {last_occ_of_a}")

#Challenge - 6;
# password = input("Enter your password: ")

# has_whitespace = password != password.strip()
# has_special_char = "@" in password or "#" in password or "$" in password

# if len(password) < 8:
#     print("Invalid")
# elif has_whitespace:
#     print("Invalid")
# elif not has_special_char:
#     print("Invalid")
# else:
#     print("Valid")

#Challenger - 7;
# name = input("Enter your name - ")
# age = int(input("Enter Your Age - "))
# #adult = age >= 18
# Country = input("Enter Your Country - ")
# is_student = input("Are You a Student? (yes/no) - ").lower().strip() in ('y', 'yes') 
# has_whitespace = name != name.strip()
# capitalize = name.capitalize()
# print(f"done with name {has_whitespace}, {capitalize}.")
# print(f"age is - {age}.")
# print("Eligible" if "Bangladesh" in Country and age >= 18 else "Not Eligible")
# #print("Eligible" if adult else "Not Eligible.")
# print("Student Status : Student" if is_student else "Student Status : Not Student") 