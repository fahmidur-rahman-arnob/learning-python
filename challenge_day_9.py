#challenge: 1 -> Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle' or not

# f = open("poems.txt", "r")

# content = f.read()

# if "twinkle" in content : 
#     print("Twinkle is there in peoms file.")
# else :
#     print("Twinkle is not there in poems file.")

# f.close()

#Challenge: 2 -> the game() func in a program let's a user play a game and returns the score as an integer. you need to read a file "Hi-Score.txt" which is either blank or contains the previous high score. you need to write a program to update the high-score whenever the game() function breaks the high-score.
# import random
# def game() :

#     print("You're playing the game...")
#     score = random.randint(1, 62)
#     #fetch the high score
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else :
#             hiscore = 0

#     print(f"Your Score: {score}")
#     if(score > hiscore) : 
#         #write this hiscore to the file
#         with open("hiscore.txt", "w") as f :
#             f.write(str(score))
#     return score

# game()

#Challenge: 3 -> write a program to generate multiplication tables from 2 to 20 and write it to the different files. place these files in a folder for a 13-years old.

# def generate_table(n) : 
#     table = ""
#     for i in range(1, 11) : 
#         table += f"{n} X {i} = {n * i}\n"
#     with open(f"tables/table_{n}", "w") as f:
#         f.write(table)

# for i in range(2, 21) :
#     generate_table(i)

#Challenge: 4 -> a file contains a word "donkey" multiple times. You need to write a program which replace the word with ###### by updating the same file.
# word = "Donkey"

# with open("file.txt", "r") as f:
#     content = f.read() #reading the content

# content_new = content.replace(word, "######")

# with open ("file.txt", "w") as f :
#     f.write(content_new)

# -----------------------------
# another version of the above program 
#words = ["Donkey", "ganda", "chut*i puda", "nubbi chusha"]

#with open("file.txt", "r") as f:
    #content = f.read() #reading the content

#for word in words : 
    #content = content.replace(word, "#" * len(word)) #updating the same variable 
    # "#" * len(word) -> meaning holo word er length joto thakbe toto gulo # sign jate word e chole ashe ... more of a programming way of saying normal stuff.

#with open ("file.txt", "w") as f :
    #f.write(content) #updated variable goes here


#Challenge: 5 -> write a program to mne a log file and find out whether it contains 'python'.
# with open("log.txt", "r") as f :
#     content = f.read()

# if("Python" in content ) : 
#     print("Yes! Python is present.")
# else : 
#     print("No! Python is not present.")

#Challenge: 6 -> an updated version of program 5 write the line number on which python is present.

# with open("log.txt") as f: 
#     lines = f.readlines() #reading each line in order to see if that line has python in it or not

# line_num = 1
# for line in lines :
#     if ("Python" in line) :
#         print(f"Yes! Python is present on line no. {line_num}.")
#         break
#     line_num += 1

# else : 
#     print("No! Python is not present.")

#Challenge: 7 -> Write a program to make a copy of a text file this.txt

# with open("this.txt", "r") as f: 
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)