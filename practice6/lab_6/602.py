n=int(input())
a=map(int,input().split())
even_number=list(filter(lambda x: x%2==0,a))
print(len(even_number))