n=int(input())
a=list(map(str,input().split()))
print(max(a,key=len))