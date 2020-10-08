import turtle
import random

mandala=turtle.Turtle()
mandala.speed(0)

colors=['gold','red','blue','green','pink','turquoise','purple','orange','white']

length=500
angle=91
circle_size=10

for side in range(length):
    #print(side)
    color=random.choice(colors)
    mandala.pencolor(color)
    mandala.fillcolor(color)
    mandala.penup()
    mandala.forward(side)
    mandala.pendown()
    mandala.left(angle)
    mandala.begin_fill()
    mandala.circle(circle_size)
    mandala.end_fill()

turtle.exitonclick()
