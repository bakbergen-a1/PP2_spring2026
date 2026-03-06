names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# 1. enumerate() - index and name
for index, name in enumerate(names):
    print(f"{index}: {name}")

# 2. enumerate() with start=1
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")

# 3. zip() - name and score
for name, score in zip(names, scores):
    print(name, score)

# 4. zip() - create dictionary
score_dict = dict(zip(names, scores))
print("Score dictionary:", score_dict)

# 5. sorted() and  type conversion
nums = [5, 2, 9, 1]
print("Sorted:", sorted(nums))
str_nums = list(map(str, nums))
print("As strings:", str_nums)