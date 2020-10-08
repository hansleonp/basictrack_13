import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for element in range(12):
    leonardo.color(colors[element % len(colors)])
    leonardo.forward(50)
    leonardo.left(30)

paper.exitonclick()