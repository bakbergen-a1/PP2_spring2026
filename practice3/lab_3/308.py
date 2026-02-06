def cal(n,m):
    if n>=m:
        print(n-m)
    else:
        print("Insufficient Funds")
b,w=map(int,input().split())
cal(b,w)