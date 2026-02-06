def show(x, y):
    print(f"({x}, {y})")

def dist(a, b):
    print(f"{(a**2 + b**2)**0.5:.2f}")
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x0 = x3 - x2
y0 = y3 - y2
show(x1, y1)
show(x2, y2)
dist(x0, y0)
