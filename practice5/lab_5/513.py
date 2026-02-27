import re
a=input()
reg=re.findall(r"\w+",a)
print(len(reg))