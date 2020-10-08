import turtle
window = turtle.Screen()
window.bgcolor('lightgreen')
window.title('Square')
alex= turtle.Turtle()
tess = turtle.Turtle()
tess.color('red')
alex.shape('turtle')
alex.speed(10)

for _ in range(4):
    alex.forward(50)
    alex.left(90)
tess.penup()
size=20
for _ in range (5):
    tess.stamp()
    size=size+20
    tess.forward(size)
    tess.right(24)

window.exitonclick()