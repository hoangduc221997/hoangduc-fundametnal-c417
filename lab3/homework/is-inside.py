def is_inside(x, y):
    if 140 <=x and x <= 240 and 60 <=y and y <=260:
        print(True)
        return(True)
    else:
        print(False)
        return False

x = int(input("Toa Do X: "))
y = int(input("To do Y: "))
is_inside(x,y)
