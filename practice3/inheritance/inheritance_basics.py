class Parent:
    def speak(self):
        print("Parent")

class Child(Parent):
    pass

Child().speak()

class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    pass

Dog().sound()

class A:
    def show(self):
        print("A")

class B(A):
    pass

B().show()

class Person:
    def info(self):
        print("Person")

class Student(Person):
    pass

Student().info()

class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

Car().move()
