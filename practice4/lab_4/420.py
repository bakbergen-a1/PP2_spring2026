import sys

n = int(sys.stdin.readline().strip())

g = 0
n_outer = 0
local_var = 0

for _ in range(n):
    line = sys.stdin.readline().strip().split()
    scope = line[0]
    value = int(line[1])
    
    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n_outer += value
    elif scope == "local":
        local_var += value

print(f"{g} {n_outer}")