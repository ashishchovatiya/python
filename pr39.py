import turtle

polygon = turtle.Turtle()
polygon.shape('turtle')
num_sides = 200
side_length = 1
angle = 360.0 / num_sides
polygon.speed(0)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
    #polygon.right(angle)
for i in range(num_sides):
    polygon.forward(side_length+1)
    polygon.left(angle)
for i in range(num_sides):
    polygon.forward(side_length+2)
    polygon.left(angle)
for i in range(num_sides):
    polygon.forward(side_length+3)
    polygon.left(angle)
#turtle.done()
turtle.exitonclick()