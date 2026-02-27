import re
a=input()
pattern=re.compile(r"^\d+$")
x=pattern.search(a)
if x:
    print("Match")
else:
    print("No match")