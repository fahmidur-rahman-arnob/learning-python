#challenge - 1;
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turky"]]
# you_want = input("Enter what you're searching: ")

# for rows in groceries : 
#     for items in rows :
#         if items == you_want : 
#             print("Item Found.")
#             break
#         else :
#             print("Item not found.")
#             break
#     if you_want :
#         break

#Challenge - 2;
# numbers = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [100, 200, 300]
# ]
# for nums in range(len(numbers)):
#     total = 0
#     for num in numbers[nums] :
#         total += num
#     print(f"Sum of row {nums} : {total}")

#Challenge - 3;
# marks = {
#     "Arnob": 85,
#     "Rahim": 72,
#     "Karim": 91,
#     "Sakib": 68,
#     "Nabil": 85
# }
# get_mark = input("Enter students name: ")

# if get_mark in marks :
#     print(f"{get_mark} marks is {marks.get(get_mark)}")
# else : 
#     print("Student not found.")

#challenge - 4;
# marks = {
#     "Arnob": 85,
#     "Rahim": 72,
#     "Karim": 91,
#     "Sakib": 68,
#     "Nabil": 85
# }
# #hishab korar jonno prathomik variable
# total_student = 0
# total_mark = 0

# #highest & lowest mark track korar jonno dict. er first value diye start kora jete pare
# #loop er vitore compare korte jate easy hoy shejonno
# first_student = list(marks.keys())[0]
# highest_mark = marks[first_student]
# lowest_mark = marks[first_student]

# for student, mark in marks.items():
#     total_student += 1 # jokhon protibar loop ghurbe tokhon student er count 1 increase hobe
#     total_marks += mark # total mark jog hocche eta sum() method er kajta korche r ki 

#     #ekhon highest mark check korar jonno
#     if mark > highest_mark : 
#         highest_mark = mark

#     #ekhon lowest mark check korar jonno 
#     if mark < lowest_mark : 
#         lowest_mark = mark
    
# #average mark hishab kora 
# average_mark = total_marks / total_student

# #ekhon result print korbo using f-string
# print(f"total student - {total_student}")
# print(f"highest mark - {highest_mark}")
# print(f"lowest mark - {lowest_mark}")
# print(f"average mark - {average_mark:.2f}")#decimal er pore 2 ghor porjonto dekhanor jonno

#challenge - 5;
# students = {
#     "Arnob": {"age": 24, "mark": 85},
#     "Rahim": {"age": 23, "mark": 72},
#     "Karim": {"age": 25, "mark": 91}
# }
# name = input("Enter The name you want to search - ")

# info = students.get(name)

# if info :
#     print(f"Age : {info['age']}")
#     print(f"Mark : {info['mark']}")
# else :
#     print("Student Not Found.")


#Challenge - 6;
# numbers = [
#     [10, 20, 10],
#     [30, 20, 10],
#     [40, 30, 20]
# ]

# freq = {}

# for row in numbers : 
#     for num in row :
#         if num in freq :
#             freq[num] += 1
#         else : 
#             freq[num] = 1
# for num, count in freq.items() :
#     print(f"number {num} appears {count} times.")

#Challenge - 7;
# products = {
#     "Laptop": 80000,
#     "Mouse": 1500,
#     "Keyboard": 3000,
#     "Monitor": 25000,
#     "Headphone": 5000
# }
# for product, price in products.items():
#     print(f"{product} : {price} TK.")

# total_products = 0
# total_price = 0

# first_product = list(products.keys())[0]
# expensive_product = first_product
# expensive_price = products[first_product]

# cheap_product = first_product
# cheap_price = products[first_product]

# for product, price in products.items():
#     total_products += 1
#     total_price += price
#     if price > expensive_price :
#         expensive_price = price 
#         expensive_product = product
#     if price < cheap_price : 
#         cheap_price = price
#         cheap_product = product

# average_price = total_price / total_products
# print(f"Product Count {total_products}")

# print(f"expensive product - {expensive_product} is {expensive_price} TK.")

# print(f"Cheap Product {cheap_product} is {cheap_price} TK.")
# print(f"average price {average_price:.2f} TK.")