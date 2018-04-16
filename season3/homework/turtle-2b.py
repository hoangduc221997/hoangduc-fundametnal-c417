from turtle import *
colors = ["red","blue","brown","yellow","gray"]
for i in range(5):
    begin_fill()
    color(colors[i])
    for j in range(2):
        forward(20)
        left(90)
        forward(40)
        left(90)
    forward(20)
    end_fill()
mainloop()
