from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map() - возведение в квадрат
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# 2. map() - удвоение чисел
doubled = list(map(lambda x: x*2, numbers))
print("Doubled:", doubled)

# 3. filter() - оставить только чётные
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# 4. filter() - оставить числа больше 3
greater_than_3 = list(filter(lambda x: x > 3, numbers))
print("Numbers > 3:", greater_than_3)

# 5. reduce() - сумма всех чисел
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)