def cycle_generator(lst, n):
    for i in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())

result = list(cycle_generator(lst, n))
print(*result)