'''
default arguments = A default value for certain parameters defult is used when that arguments is omitted make your functions more flexible, reduce number of argument 
1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

'''


def net_price(list_price, discount=0, tax=0.05) :
    final_price = list_price * (1 - discount) * (1 + tax)
    return f"{final_price:.1f}"

#print(net_price(500)) -> with default arguments, although this function can take upto 2 more arguments ... let's imagine a scenario when discount is greater than 0 and tax is more than 0.05 percent.

#print(net_price(500, 0.1)) # if we're passing in a argument for our discount(which is a default value) then we'll use whatever is passed in rather than using the default

#print(net_price(500, 0.1, 0)) # this time we're not paying any tax's

#ex - we'll create a count up timer
#import time # default module of python

#def count (end, start = 0) :
    #for x in range(start, end + 1) : #within tthe range function the second argument is exclusive, which means you've to add 1 with it to get the real value.
        #print(x)
        #time.sleep(1) # this method makes the thread that running the program sleep for the passed value; in this case it'll sleep for 1 second.
    #print("DONE!")

#count(6)


'''
keyword arguments = an argument preceded by an identifier helps with readability 
order of arguments doesn't matter
1. positional 2. default 3. KEYWORD 4. arbitrary
'''
#def hello(greeting, title, first_name, last_name) :
    #print(f"{greeting} {title}{first_name}{last_name}")

#hello("Hello", title="Mr.", first_name="Spongebob", last_name="Squarepants")
#hello(last_name="Arnob", greeting="Hello", first_name="Fahmidur Rahman ", title="Mr.")

# for x in range(1, 10+1) : 
#     print(f"x is - {x}", end=" ")

# print("1", "2", "3", "4", "5", sep="-")

#example - we're going to create a function to generate a phone number but we'll have to provide country code andd first few digits last few digits

#def get_phone (country_code, area_code, first_few, last_few) : 
    #return f"{country_code}-{area_code}-{first_few}-{last_few}"

# print(get_phone("+88","01", "959", "83")) #This is one way

# my_phone = get_phone(country_code=+880, area_code=19, first_few=5938, last_few=1083)

# print(my_phone)


'''
*args = allows you to pass multiple non-key arguments, in tuple
**kwargs = allows you to pass multiple keyword-arguments, in dict.
* -> unpacking operator
1. positional 2. default 3. keyword 4. arbitrary

'''
# def add (a, b) :
#     return a + b

# print(add(5, 6, 9))

#def add(*args) : #you cann change the args to something else as well like something relevant ... but make sure to put * before it... one * means args and two * means kwargs.
    # return a + b 
    #total = 0
    #for arg in args :
        #total += arg
    #return total

#print(add(1))

# def display_name(*args) :
#     for arg in args :
#         print(arg, end=" ")

# display_name("Python Guru", "Fahmidur", "Rahman", "Arnob")

#kwargs
#def print_address (**kwargs) : 
    #pass # pass doesn't do anything
    #print(type(kwargs))
    # for value in kwargs.values() : 
    #     print(value, end=" ")
    # for key in kwargs.keys() : 
    #     print(key, end=' ')
    #for key, value in kwargs.items() : 
        #print(f"{key}: {value},",)

# print_address(street="123 Fake St. ", 
#               city="Detroit", 
#               state="MI", 
#               zip="54321",
#               apt="40")


#ex: 
#def shipping_label (*args, **kwargs) : #kwargs follows args, it wont work other way around... meaning kwargs comes after args...
    #lets iterate over args first
    # for arg in args : 
    #     print(arg, end=" ")
    # print()
    # for key, value in kwargs.items() : 
    #     print(f"{key}: {value}")

# shipping_label("Python Guru", "Md", "Fahmidur", "Rahman", "Arnob",
#                street="123 Fake St.",
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321",
#                timezone="GMT+6:40")