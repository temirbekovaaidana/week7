 # #frozenset

 # #set
 # set_a = [1, 2, 3 , 4, "Nazgul"]
 # frozenset_2 = frozenset(set_a)
 # frozenset_1 =
 #
 #
 # # zip
 # # 4 встроенных функций которые часто используются
 #
# list1 = ["apple", "banana"]
# list2 = ["tomato", "potato"]
# print(list(zip(list1, list2)))
# print(dict(zip(list1, list2)))

#рекурсия
# number: int = int(input("give number: "))
# for i in range(1, number + 1):
#     print(i)

# def recursion_counter(number):
#     if number == 0:
#         return number
#     else:
#         print(number)
#         return recursion_counter(number - 1)
# print(recursion_counter(number))

# number: int = int(input("give number: "))
# def get_factorial(number):
#     if number == 1:
#         return 1
#     else:

#         return number * get_factorial(number - 1)
# print(get_factorial(number))

# list_a = [1, 2, 3]
# def get_sum_list(lists):
#     if lists == []:
#         return 0
#     else:
#         get_result = get_sum_list(lists[1:])
#         summ = get_result + lists[0]
#         print(summ)
#         return summ
# get_sum_list(list_a)

# counter = 0
# for i in range(1, 5):
#      counter += i
# print(counter)

# json
import json
with open("test1.json", "r") as file:
    new_dict = json.load(file)

new_dict["name"] = "Zamira"
new_dict["age"] = 17
new_dict["is_18"] = False

with open("test1.json", "w") as file:
    text_json = json.dumps(new_dict, indent=4)
    print(text_json)
    file.write(text_json)

