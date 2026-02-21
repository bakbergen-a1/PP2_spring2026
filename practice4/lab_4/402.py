'''def my_generator(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
a=list(my_generator(n))
print(','.join(map(str,a)))''',

#n=int(input())
#print(','.join(str(i) for i in range(0,n+1,2)))

def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

res=[]
n=int(input())
for x in even(n):
    res.append(str(x))
print(",".join(res))
    