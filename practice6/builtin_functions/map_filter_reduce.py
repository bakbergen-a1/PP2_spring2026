from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map() - squaring
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# 2. map() - doubling numbers
doubled = list(map(lambda x: x*2, numbers))
print("Doubled:", doubled)

# 3. filter() - leave only even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# 4. filter() - leave numbers greater than 3
greater_than_3 = list(filter(lambda x: x > 3, numbers))
print("Numbers > 3:", greater_than_3)

# 5. reduce() - the sum of all the numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)