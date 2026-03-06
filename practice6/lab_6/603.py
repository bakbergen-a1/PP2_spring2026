n=int(input())
a=list(map(str,input().split()))
for index, name in enumerate(a):
    print(f"{index}:{name}",end=" ")
