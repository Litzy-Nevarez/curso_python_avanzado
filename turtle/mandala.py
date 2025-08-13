import turtle

colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']
turtle.speed(0)

for i in range(36):
    turtle.color(colors[i % len(colors)])
    turtle.circle(100)
    turtle.left(10)

turtle.done()
