import math

def compare(x, y):
    if (x > y):
        return 1
    elif (x == y):
        return 0
    else:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    #print('dsquared is:', dsquared)
    #print('dx is:', dx)
    #print('dy is:', dy)
    return math.sqrt(dsquared)

def area(r):
    return math.pi * r**2

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    return area(radius)

print(circle_area(1, 2, 4, 6))
#print(distance(1, 2, 4, 6))
#print(compare(1, 2))