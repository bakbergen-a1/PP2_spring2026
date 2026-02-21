import math

R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

d1 = math.hypot(x1, y1)
d2 = math.hypot(x2, y2)

direct = math.hypot(x2 - x1, y2 - y1)

if d1 >= R and d2 >= R:
    v = (x2 - x1, y2 - y1)
    t = -(x1*v[0] + y1*v[1]) / (v[0]*v[0] + v[1]*v[1]) if (v[0]*v[0] + v[1]*v[1]) != 0 else 0
    
    if 0 <= t <= 1:
        cx = x1 + t * v[0]
        cy = y1 + t * v[1]
        dist = math.hypot(cx, cy)
        
        if dist < R:
            l1 = math.sqrt(d1*d1 - R*R)
            l2 = math.sqrt(d2*d2 - R*R)
            
            theta1 = math.atan2(y1, x1)
            theta2 = math.atan2(y2, x2)
            
            alpha1 = math.acos(R / d1)
            alpha2 = math.acos(R / d2)
            
            theta1a = theta1 - alpha1
            theta1b = theta1 + alpha1
            theta2a = theta2 - alpha2
            theta2b = theta2 + alpha2
            
            def arc_length(t1, t2):
                diff = abs(t1 - t2)
                diff = min(diff, 2*math.pi - diff)
                return R * diff
            
            path1 = l1 + arc_length(theta1a, theta2a) + l2
            path2 = l1 + arc_length(theta1a, theta2b) + l2
            path3 = l1 + arc_length(theta1b, theta2a) + l2
            path4 = l1 + arc_length(theta1b, theta2b) + l2
            
            result = min(path1, path2, path3, path4)
            print(f"{result:.10f}")
        else:
            print(f"{direct:.10f}")
    else:
        print(f"{direct:.10f}")
else:
    print(f"{direct:.10f}")