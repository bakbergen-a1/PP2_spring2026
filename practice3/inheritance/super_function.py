class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

Child()

class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("Meow")

Cat().sound()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

B().show()

class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        super().greet()
        print("Student")

Student().greet()

class X:
    def run(self):
        print("Run X")

class Y(X):
    def run(self):
        super().run()
        print("Run Y")

Y().run()
