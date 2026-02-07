class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()

class Person:
    def work(self):
        print("Working")

class Teacher(Person):
    def work(self):
        print("Teaching")

Teacher().work()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

B().show()

class Vehicle:
    def move(self):
        print("Move")

class Bike(Vehicle):
    def move(self):
        print("Bike moving")

Bike().move()

class Shape:
    def draw(self):
        print("Drawing")

class Circle(Shape):
    def draw(self):
        print("Circle")

Circle().draw()
