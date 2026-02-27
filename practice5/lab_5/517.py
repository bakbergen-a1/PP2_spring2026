import re

a = input()
reg = r"\b\d{2}/\d{2}/\d{4}\b"  
matches = re.findall(reg, a)
print(len(matches))