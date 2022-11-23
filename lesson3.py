temperature = int(input("Ввeдите температуру в Цельсиях: "))
if temperature < -273.15:
  print("температура недействительна, потому что она ниже абсолютного нуля.")
if temperature == -273.15:
  print("температура равна абсолютному 0")
if temperature > -273.15 and temperature < 0:
  print("температура ниже точки замерзания")
if temperature == 0:
  print("температура находится в точке замерзания")
elif temperature >0 and temperature < 100:
  print("температура находится в нормальном диапазоне")
elif temperature == 100:
  print("температура находится в точке кипения")
elif temperature >100:
  print("температура выше точки кипения")


## class
## моносостояние

# class Car:
#   _property_cars = {
#     "model": "vaz",
#     "color": "blue"
#   }
#   def __init__(self):
#     self.__dict__ = Car._property_cars
# car1 = Car()
# car2 = Car()
# print(car2.__dict__)
# print(car1.__dict__)
# print(car1.model)
# car2.model = "volga"
# print(car1.model)
# print(car2.model)

## dunder methods eq hash
## equal

# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#
#   def __eq__(self, other):
#     if isinstance(other, Point):
#       return self.x == other.x and self.y == other.y
#
#   def __hash__(self):
#     return hash((self.x, self.y))
# point1 = Point(12, 6)
# point2 = Point(12, 6)
# # print(point1 == point2)
# print(hash(point1))
# print(point1.__hash__())
# print(hash(point2))
# print(id(point1))
# print(id(point2))
# print(id(None))
# print(id(null))

## Mixin
## datetime

# users = {}
# class RegisterMixin:
#   def validate_username(self):
#     if self.username in users.keys():
#       print("Такой пользователь уже существует!!!")
#       return False
#     return True
# class Register(RegisterMixin):
#   def __init__(self, name, age, username):
#     self.name = name
#     self.username = username
#     self.age = age
#
#   def save_to_dict(self):
#     users.update({
#       self.username: {
#       "name": self.name,
#       "age": self.age,
#     }})
#
#   def save_in_validated_data(self):
#     if self.validate_username():
#       self.save_to_dict()
#       return "Succesfuly saved {0}!!!".format(self.username)
#     return "Didn't save {0}!!!".format(self.username)
#
# nazgul = Register("nazgul", 26, "aveid")
# print(nazgul.save_in_validated_data())
# chyngyz = Register("chyngyz", 20, "chika")
# print(chyngyz.save_in_validated_data())
# syimyk = Register("Syimyk", 18, "aveid")
# print(syimyk.save_in_validated_data())
# print(users)

# class Investment:
#   def __init__(self, principal, interest):
#     self.principal = principal
#     self.interest = interest
#
#   def __str__(self):
#     return f"Основная сумма - {self.principal} долларов США, процентная ставка - {self.interest}%"
#
#   def value_after(self):
#     n = int(input('Years: '))
#     return self.principal * (1 + self.interest) * n
#
# object = Investment(1000, 15)
# print(object.value_after())
# print(object)
#
# class Product:
#   def __init__(self, name, stock_amount, price):
#     self.name = name
#     self.stock_amount = stock_amount
#     self.price = price
#
#   def get_price(self, amount: int):
#     if amount <= 10:
#       return self.price * amount
#     elif amount > 10 and amount < 100:
#       return (self.price * amount) - ((self.price * amount) / 100)* 10
#     elif amount >= 100:
#       return self.price * amount * 0.8
#
# apple = Product("apple", 100, 80)
# print(apple.get_price(120))
