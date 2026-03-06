n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=[]
for x,y in zip(a,b):
    m.append(x*y)
print(sum(m))