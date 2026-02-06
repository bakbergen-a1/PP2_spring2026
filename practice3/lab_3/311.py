def addition(x, y):
    return x + y

a1, b1, a2, b2 = map(int, input().split())
a = addition(a1, a2)
b = addition(b1, b2)
print(f"Result: {a} {b}")
