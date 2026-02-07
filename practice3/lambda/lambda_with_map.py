nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))

names = ["ali", "dana"]
print(list(map(lambda x: x.capitalize(), names)))

values = [5, 10]
print(list(map(lambda x: x + 1, values)))

data = [2, 4, 6]
print(list(map(lambda x: x / 2, data)))

ages = [18, 20]
print(list(map(lambda x: x >= 18, ages)))
