class A:
    def show(self):
        print("A")

class B:
    def show2(self):
        print("B")

class C(A, B):
    pass

C().show()
C().show2()

class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

d = Duck()
d.fly()
d.swim()

class X:
    def x(self):
        print("X")

class Y:
    def y(self):
        print("Y")

class Z(X, Y):
    pass

Z().x()
Z().y()

class Teacher:
    def teach(self):
        print("Teach")

class Researcher:
    def research(self):
        print("Research")

class Professor(Teacher, Researcher):
    pass

p = Professor()
p.teach()
p.research()

class A1:
    def a(self):
        print("A1")

class B1:
    def b(self):
        print("B1")

class C1(A1, B1):
    pass

c = C1()
c.a()
c.b()
