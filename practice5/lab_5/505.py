import re
a=input()
reg=r"^[A-Za-z].*[0-9]$"
r=re.match(reg,a)
if r:
    print("Yes")
else:
    print("No")
    