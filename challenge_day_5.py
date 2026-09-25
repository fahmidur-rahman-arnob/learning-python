#challenge - 1;
# numbers = [4, 7, 2, 4, 9, 7, 4, 10, 2]
# list_numbs = set(numbers)
# print(type(list_numbs))
# print(list_numbs)

#challenge - 2;
# lang = {"python", "c", "c++", "java", "rust"}
# user_lang = input("Enter Your Programming Language: ").lower().strip()
# if user_lang in lang :
#     print("Found")
# else : 
#     print("Not Found")

#Challenge - 3;
# subjects = ("Python", "Math", "English", "Statistics", "SQL")
# middle_sub_index = len(subjects) // 2
# middle_sub = subjects[middle_sub_index]
# print(subjects[0])
# print(subjects[-1])
# print(middle_sub)
# print(subjects[0:3])
# print(subjects[::-1])

#Challenge - 4;
#colors = ("red", "green", "blue")
#colors[1] = "yellow"
#print(colors)#typeerror...because tuples are immutable we can't change or modify a value in tuple...

#Challenge - 5;
# this_is_set = {"apple", "apple", "guava", "orange", "cherry"}
# this_is_tuple = ("apple", "apple", "guava", "orange", "cherry")

# 1. tuple e dupli. thake
# 2. set e dupli. automatically chole jay
# 3. tuple e indexing kora jay
# 4. set e indexing kora jay na 

#Challenge - 6;
#numbers = [10, 20, 10, 30, 40, 20, 50, 30, 10]
#new_nums = [] # empty list to store unique values

#for nums in numbers : #eta list er iterate korbe and value check korbe
    #if nums not in new_nums : # tarpor dekhbe j num jodi new_nums list e thake tahole append method er maddhome shei unique number ta new_nums e entry dibe... first time jokhon run korbe tokhon jehetu amdr new_nums[] list ta empty thakbe tokhon first number ta emnitei chole jabe new_nums list e .. tapor jokhon abr iterate hobe tokhon new_nums list er already exited values er sathe match kore dekhbe jodi sheta already new_nums e exist kore tahole ignore korbe nahole shetake append korbe
        #new_nums.append(nums)
# ekhon amra count korbo j new_nums listt e koyta unique items ache ... len method er maddhome
#unique = len(new_nums)
#print(unique)