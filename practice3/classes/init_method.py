class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)

class Student:
    def __init__(self, age):
        self.age = age

s = Student(18)
print(s.age)

class Car:
    def __init__(self, brand):
        self.brand = brand

print(Car("Mersedes").brand)

class Book:
    def __init__(self, title):
        self.title = title

print(Book("Python").title)

class City:
    def __init__(self, name):
        self.name = name

print(City("Almaty").name)
