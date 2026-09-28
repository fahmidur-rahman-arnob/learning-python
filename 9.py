'''
if __name__ == __main__ :(This script can be imported OR run standalone) -> functions and classes in this module can be reused without the main block of code executing

Before running a Python file, the interpreter sets a few special variables. One of them is __name__.

If a Python file is run directly, Python sets __name__ to "__main__".
If the same file is imported into another file, __name__ is set to the module’s name.
A module is simply a Python file (.py) that contains functions, classes, or variables.

This statement is commonly used to make Python files more flexible and reusable. It allows a file to behave differently when it is run directly and when it is imported into another program.

Without __main__ Check
When a function is called directly in a file, it runs every time the file is executed or imported. This can lead to unwanted behavior when the file is meant to be used as a module.
    def my_func() :
        print("I am inside function")
    my_func()

output: I am inside function.
Explanation: Here, my_function() runs immediately. Even if this file is imported into another script, the function will still execute, which is usually not desired.

Better Approach Using __main__
A better and cleaner approach is to place function calls inside the if __name__ == "__main__": block.

def my_func() :
    print("I am inside func.")
if __name__ == "__main__" : 
    my_func()

output : I am inside function

Explanation:
The function runs only when the file is executed directly.
If the file is imported, the function is defined but not executed.

'''

#Tried to understand ... but didn't put that much focus on it ... but got the main idea tho 
# def main() :
#     #your code goes here
#     print("Hello from main.")

# if __name__ == '__main__' :
#     main()

# the most ***IMPORTANT*** topic --- FILE I/O ->
'''
File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.
It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

                    
                    Need for File Handling
Store data permanently, even after the program ends.
Access external files like .txt, .csv, .json, etc.
Process large files efficiently without using much memory.
Automate tasks like reading configs or saving outputs.

                        Opening a File
To open a file, we can use open() function, which requires file-path and mode as arguments. mode such as r = read, w = write, a = append etc. NOTE -> if you dont specify the mode, python uses 'r' (read mode) by default.

                    Volatile & Non-Volatile
Ram = volatile -> more fast
HDD = non volatile -> slow
the random access memory is volatile, and all it's contents are lost once a program terminates in order to persists the data forever so we use files to store that data permanently.

a file is data stored in a storage device. a python program can talk to the file by reading content from it and writing content to it

                        TYPE OF FILE
There are mainly 2 types of file:
1. text files(.txt, .c etc)
2. binary file(.jpg, .dat etc)

PYTHON has a lot of functions for reading, updating and deleting files.

r = open for reading
w = open for writing
a = open for appending
+ = open for updating
rb = will open for read in binary mode
rt = will open for read in text mode

we can also use f.readline() function to read one full line at a time. this will read one line from the file.

'''

#f = open("file.txt", "r") #open is a built-in function in python which helps to open a file
#data = f.read() # this also a built-in function in python which helps to read a file, this will come to use to know what's inside a file. as the name suggest this func reads whats inside a file(any file)
#print(data)
#f.close()# this is also a built-in function in python, this close the function.
# you MUST close after doing any operation inside a file. THIS IS A MUST, dont ask why just make it a practice. closing basically means that you're telling the computer that you're done with your task/work on this file and now you want to close the program.

#writing to a file
#st = "Hey Fahmidur, You're the new Python Guru." #string can be of any length, doesn't matter...first e ekta string nilam
#f = open("my_file.txt", "w") #we're writing to a file, that's why 'w'. 'w' means = write -> then ekta file openn korlam

#f.write(st) # now writing to that file with write function .. f.write() string ney..I dont think you can pass any other data type to write function

#f.close() # writing is done and now we're closing the program.


#more file I/o stuffs
f = open("file.txt", "r") #file name needs to be inside double quotes.

lines = f.readlines() # this will returns a list

# print(type(lines))
print(lines)

f.close()