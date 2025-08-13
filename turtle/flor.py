import turtle

turtle.color("red")
turtle.speed(0)

for _ in range(36):
    for _ in range(2):
        turtle.circle(100, 60)
        turtle.left(120)
    turtle.left(10)

turtle.done()
