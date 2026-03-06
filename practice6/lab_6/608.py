n=int(input())
a=map(int,input().split())
s=sorted(set(a))
print(*s)