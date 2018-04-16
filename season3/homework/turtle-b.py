from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    color(colors[i])
    for j in range(i+3):
        forward(50)
        left(360/(i+3))
mainloop()
