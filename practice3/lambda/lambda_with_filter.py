nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))

ages = [12, 18, 21]
print(list(filter(lambda x: x >= 18, ages)))

words = ["hi", "hello"]
print(list(filter(lambda x: len(x) > 2, words)))

marks = [40, 60, 80]
print(list(filter(lambda x: x >= 50, marks)))

values = [-1, 2, -3]
print(list(filter(lambda x: x > 0 or x==-3, values)))
