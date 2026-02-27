import re
a=input()
pattern=re.compile(r"\w+")
print(len(re.findall(pattern,a)))