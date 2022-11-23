#regular expressions

import re
# match --is text started with?

# text = "I lo ve Bishkek nazgul94.kg@gmail.com love!"
# x = re.match("I", text)
# print(x.group(0))
#
# # search -- finds the first word in the text
# x = re.search("love", text)
# print(x.group(0))
#
# x = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
# print(x.group(0))

# x = re.findall(r"^[l-o]$", text)
# print(x)

# with open("pushkin.txt") as stih:
#     oda = stih
# word1 = re.findall(r"спящий", oda)
# word2 = re.findall(r"бичи", oda)
# print(word1)
# print(word2)

# text = "I lo ve Bishkek nazgul94.kg@gmail.com ve love!"
# x = re.split("lo", text, maxsplit=2)
# print(x)

# x = re.sub("lo", "gg", text, count=2)
# print(x)
# x = re.sub("lo | ve", "gg", text)
# print(x)

# with open("zadacha.txt", "r") as file:
#     numbers = file.read()
#     x = re.findall(r"(\+996\(5{2}[0-9]\)[-]+[0-9]{3}-+[0-9]{3})", numbers)
#     y = ' '.join(x)
#     z = re.sub("-", " ", y)
#     print(z)
# with open("numbers.txt", "w+") as file:
#     file.write(z)

with open("zadacha.txt", "r") as file:
    text = file.read()
    numbers = re.findall("\+996\(5{2}[0-9]\)[-]+[0-9]{3}-+[0-9]{3}", text)
    for i in numbers:
        str_rep = i.replace("-", " ")
        text = text.replace(i, str_rep)
    print(text)
with open("numberss.txt", "w") as file:
    file.write(text)