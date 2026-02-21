def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input().strip())

if n <= 0:
    print()
else:
    fib_numbers = list(fibonacci_generator(n))
    print(','.join(map(str, fib_numbers)))