def generator(n):
    for i in range(n+1):
        yield 2**i
n=int(input())
for i in generator(n):
    print(i,end=" ")
    