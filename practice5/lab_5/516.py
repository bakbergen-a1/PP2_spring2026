import re

a = input()
reg = r"Name: ([^,]+), Age: (\d+)"
x = re.search(reg, a)

if x:
    print(' '.join(x.groups()))