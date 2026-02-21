#iter() and next()
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

#iterator class 
class Counter:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

counter = Counter()

for x in counter:
    print(x)

#generator function (even numbers)
def even_numbers(n):
    for i in range(0,n+1, 2):
        yield i

for num in even_numbers(10):
    print(num)

#yield Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num)

#Generator expression
squares = (x*x for x in range(5))

for s in squares:
    print(s)