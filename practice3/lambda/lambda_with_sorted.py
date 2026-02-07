nums = [5, 2, 8]
print(sorted(nums, key=lambda x: x))

words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda x: len(x)))

pairs = [(1, 3), (2, 1)]
print(sorted(pairs, key=lambda x: x[1]))

names = ["Ali", "aigerim"]
print(sorted(names, key=lambda x: x.lower()))

scores = [70, 90, 60]
print(sorted(scores, reverse=True))
