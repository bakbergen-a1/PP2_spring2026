import re
s=input()
p=input()
reg=re.findall(p,s)
print(len(reg))