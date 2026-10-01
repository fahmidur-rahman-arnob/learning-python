'''
            Object Oriented Programming

object oriented programming empowers developers to build modular, maintainable and scalable applications. OOPO is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOP, object has attributes thing that has specific data and can perform certain actions using methods.
    -> Organizes code into classes and objects
    -> Supports encapsulation to group data and methods together.
    -> Enables inheritance for reusability and hierarchy.
    -> Allows polymorphism for flexible method implementation.

1. Class -> A blueprint or template for creating objects.

2. Objects -> an instance of a class.

3. Encapsulation -> Protects data from direct access.

4. Abstraction -> Hides unnecessary details.

5. Polymorphism -> Allows the same method to behave differently.

6. Inheritance -> Reuses code from existing classes.

                    Class

a class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects(instances) can have.
    
    -> Classes are created by the Keyword 'class'.
    -> Attributes are the variables that belong to a class.
    -> Attributes are always public and can be accessed using the dot(.) operator. Example: Myclass.Myattribute
Here, class keyword indicates that we are creating a class followed by name of the class (Dog in this case).


class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


                    Objects

An Object is an instance of a class. It represents a specific implementation of hte class and holds it's own data. an object consists of: 
    -> State: represented by the attributes and reflects the properties of an object.
    -> Behavior: Represented by the methods of an object and reflects the response of an object to other objects.
    -> Identity: Gives a unique name to an object and enables one object to interect with other objects.





'''

#basic program
# class Employee : #Employee class banaisi
#     #name = "Arnob"
#     language = "Py" # these are class attributes because they directly belong to Employee class
#     salary = 12000000

# harry = Employee() #Employee hoise harry, r harry hoise muloto ekta object.
# harry.name = "Harry" #This is a object/instance attribute
# print(harry.name, harry.language, harry.salary)

# rohan = Employee()
# rohan.name = "Rohan Roro Robinson" #This is a object/instance attribute
# print(rohan.language, rohan.salary, rohan.name)

#instance attibutes take preferance over class attributes during assignment and retrival.

#Example: 
class Employee() : 
    language = "Py"
    salary = 1200000

harry = Employee()
harry.name = "Ha Ha Harry"
harry.language = "Javascript"
print(harry.name, "\n", harry.language, "\n", harry.salary)

print("---------------------------")

rohan = Employee()
rohan.name = "Ro Ro Rohan"
rohan.language = "Rust"
print(rohan.name, "\n", rohan.language, "\n", rohan.salary)