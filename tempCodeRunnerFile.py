username = input("Enter Your Username - ")
len_of_name = len(username)
while len_of_name < 5 and username != "" and username[0] != '@' and username[-1] != '@':

    print("Valid Username")
print(f"username '{username}' is invalid.") 