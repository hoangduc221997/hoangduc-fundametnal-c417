
from turtle import *
def draw_square(len,c):
    shape("turtle")
    color(c)
    for i in range (4):
        forward(len)
        left(90)

    
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
