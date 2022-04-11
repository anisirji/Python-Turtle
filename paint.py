from turtle import Turtle,Screen
import turtle

screen = Screen()
pen = Turtle()
pen.speed(-1)
pen.pensize = 100

def pencil(x,y):
    # print(x,y)
    pen.ondrag(None)
    pen.setheading(pen.towards(x,y))
    pen.goto(x,y)
    pen.ondrag(pencil)

def clickR(x,y):
    # print(x,y)
    pen.clear()

def main():
    turtle.listen()
    pen.ondrag(pencil)
    turtle.onscreenclick(clickR,3)
    screen.mainloop()

main()