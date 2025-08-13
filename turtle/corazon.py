import turtle

turtle.color('red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(113)

turtle.circle(-57, 200)
turtle.left(120)
turtle.circle(-57, 200)

turtle.forward(112)
turtle.end_fill()

turtle.hideturtle()

turtle.penup()
turtle.goto(0, 70)
turtle.color("white")
turtle.write("Te quiero", align="center", font=("Arial", 16, "bold"))

turtle.done()