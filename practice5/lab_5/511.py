import re
a=input()
reg=re.findall(r"[A-Z]",a)
print(len(reg))