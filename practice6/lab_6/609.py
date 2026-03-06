n=int(input())
a=list(map(str,input().split()))
b=list(map(str,input().split()))
k=input()
x=[]
for name,key in zip(a,b):
    if name==k: x.append(key)
if len(x)==0:
    print("Not found")
else:
    print(*x)
        