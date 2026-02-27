import re
a=input()
reg=r"^Hello"
x=re.match(reg,a)
if x:
    print("Yes")
else:
    print("No")
