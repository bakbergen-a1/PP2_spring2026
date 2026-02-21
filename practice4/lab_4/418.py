import math

x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

if y1 * y2 > 0:
   
    x2_reflected = x2
    y2_reflected = -y2
    
    if y1 == y2_reflected:
        x = x1
    else:
        t = y1 / (y1 - y2_reflected)
        x = x1 + t * (x2_reflected - x1)
else:
    if y1 == y2:
        x = x1
    else:
        t = y1 / (y1 - y2)
        x = x1 + t * (x2 - x1)

print(f"{x:.10f} 0.0000000000")