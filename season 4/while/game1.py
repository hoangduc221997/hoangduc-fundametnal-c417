from random import *
loop = True
while loop:
    a = randint (0,100)
    print("Is", a,"your number", b)
    b = input()
if b == "l":
    a = radint(a,100)
    print("Is", a,"your nubmer", b)
elif b == "s":
    a = radint(0,a)
    print("Is", a, "your number", b)
else:
    print("sai cu phap")
