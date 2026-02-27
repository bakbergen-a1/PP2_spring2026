import re
s=input()
p=input()
reg=re.search(p,s)
if reg:
    print("Yes")
else:
    print("No")