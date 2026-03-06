n=int(input())
a=map(int,input().split())
print(sum(map( lambda x: x!=0 ,a)))