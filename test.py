import turtle
import random

pen = turtle.Turtle()
turtle.speed = 1

#star
num_of_sides = 5
length_of_side = 50

pen.bk(length_of_side/2)

each_angle = 720.0 / num_of_sides
for i in range(num_of_sides):
    pen.forward(length_of_side)
    pen.right(each_angle)


#stamp

pen.setheading(180)
pen.penup()
pen.fd(200)

def arr():
    for i in range(40, -1, -1):
        # a = random.randint(0,225)
        # b = random.randint(0,225)
        # c = random.randint(0,225)
        # turtle.colormode(255)

        # turtle.pencolor((a,b,c))
        pen.stamp()
        pen.left(i)
        pen.forward(20)
        

        


arr()

pen.goto(0,0)
pen.setheading(0)
pen.fd(200)
arr()

turtle.mainloop()