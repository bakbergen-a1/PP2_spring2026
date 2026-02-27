import re
a=input()
reg=r"\d"
r=re.sub(reg,lambda x: x.group() *2,a)
print(r)