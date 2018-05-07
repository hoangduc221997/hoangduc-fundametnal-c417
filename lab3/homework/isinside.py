def is_inside(x, y):
    if (y[0] <=x[0] <= y[0] + y[2]) and (y[1] <= x[1] <=y[1]+y[3]):
        return True
    else:
        return False
n= is_inside([1000,120],[140,60,100,200])
print(n)
