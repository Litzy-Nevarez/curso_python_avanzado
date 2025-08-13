import turtle

turtle.bgcolor("black")
turtle.speed(0)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'cyan']

for i in range(72):
    turtle.color(colors[i % 6])
    turtle.circle(100)
    turtle.left(5)

turtle.done()
