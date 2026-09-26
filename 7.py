'''
functions in python -> a block of reuseable code used to perform specific task.
-> place () after the function name to invoke it.
-> a function can be defined using the 'def' keyword
    - def function_name (parameters) :
        #statement
        return expression


'''
#ex: 


def happy_birthday () :
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

# happy_birthday()
# happy_birthday()
# happy_birthday()
# happy_birthday()
# for i in range(5) :
#     print(f"{i} ->", end=" ")
#     happy_birthday()

# with functions you're able to send a data to a function, using what are knownn as arguments you can send values or variables to a function, but remember the type of data you're sending has to be the same type of parameters the function is able to receive

# def happy_birthday(name, age) : 
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")

# happy_birthday("Arnob", 25)
# happy_birthday("Anika", 24)
# happy_birthday("Maria", 15)


#ex:- function to display an invoice with 3 parameters username, amount, due_date

def display_invoice (username, amount, due_date) :
    print(f"hello {username}.")
    print(f"your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Arnob", 43.56, "01/01/2026")