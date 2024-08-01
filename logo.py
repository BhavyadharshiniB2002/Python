import turtle
a=turtle.Turtle()
turtle.bgcolor("black")
a.pensize(10)
a.pencolor("white")
a.penup()
a.setpos(-0,-100)
a.pendown()
a.circle(150)
a.penup()
a.setpos(-60,100)
a.pendown()
# a.right(70)
a.left(130)
a.forward(10)
a.right(40)
def heart():
    for i in range(30):
        a.right(1)
        a.forward(1)
heart()



for i in range(30):
    a.right(30)
    a.forward(30)
turtle.done()


