import re
a=input()
reg=r"\d{2,}"
print(*(re.findall(reg,a)))