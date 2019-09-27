import turtle

a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()

turtle.bgcolor("light blue")

a.begin_fill()
a.fillcolor("blue")
a.up()
a.shape("turtle")
a.goto(-100,90)
a.down()
a.circle(100)
a.end_fill()

b.begin_fill()
b.fillcolor("red")
b.up()
b.shape("turtle")
b.goto(100,-90)
b.down()
b.circle(80)
b.end_fill()

c.begin_fill()
c.fillcolor("yellow")
c.up()
c.shape("turtle")
c.goto(-50,-90)
c.down()
c.left(90)
c.forward(50)
c.left(90)
c.forward(80)
c.left(90)
c.forward(50)
c.left(90)
c.forward(80)
c.end_fill()

turtle.begin_fill()
turtle.fillcolor("Green")
turtle.up()
turtle.shape("turtle")
turtle.goto(130,-190)
turtle.down()
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()







turtle.exitonclick()