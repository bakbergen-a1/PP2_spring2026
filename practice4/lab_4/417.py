import math

R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

d1_sq = x1*x1 + y1*y1
d2_sq = x2*x2 + y2*y2
R_sq = R*R

dx = x2 - x1
dy = y2 - y1
seg_len = math.hypot(dx, dy)

if seg_len == 0:
    print("0.0000000000" if d1_sq > R_sq else "0.0000000000")
    exit()

a = dx*dx + dy*dy
b = 2 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R_sq

discriminant = b*b - 4*a*c

if discriminant <= 0:
    if d1_sq <= R_sq and d2_sq <= R_sq:
        print(f"{seg_len:.10f}")
    else:
        print("0.0000000000")
    exit()

sqrt_disc = math.sqrt(discriminant)
t1 = (-b - sqrt_disc) / (2*a)
t2 = (-b + sqrt_disc) / (2*a)

t_enter = max(0, min(1, min(t1, t2)))
t_exit = min(1, max(0, max(t1, t2)))

if t_exit <= t_enter:
    print("0.0000000000")
else:
    length = (t_exit - t_enter) * seg_len
    print(f"{length:.10f}")