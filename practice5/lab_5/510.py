import re
a=input()
reg=re.search(r"cat|dog",a)
if reg:
    print("Yes")
else:
    print("No")
