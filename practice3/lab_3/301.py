def fn(n):
    s=0
    for i in n:
        if int(i)%2!=0:
            print("Not valid")
            return
    print('Valid')
n=input()
fn(n)