import re
a=input()
reg=r"\b\w{3}\b"
r=re.findall(reg,a)
print(len(r))