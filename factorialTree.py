#before runnig do "pip install PythonTurtle"
'''if error like can't find Tkinter then do "sudo apt-get install python3-tk" only for lunix'''

import turtle

pen = turtle.Turtle()

#variables
bgColor = "white"
penSize = 3
initialBranchColor = "brown"
penSpeed = 500
penShape = "turtle"
flowerColor = "red"
branchColor = "green"
branch = 1.3  #value between 0 -- 2

pen.screen.bgcolor(bgColor)
pen.pensize(penSize)
pen.color(initialBranchColor)

pen.left(90)
pen.penup()
pen.backward(250)
pen.pendown()
pen.speed(penSpeed)
pen.shape(penShape)
treeSize = 200
pen.write("ani")

#recuesive funtion to draw tree
def tree(i):
    if i<10:
        return
    else:
        pen.fd(i)
        pen.color(flowerColor)
        pen.circle(2)
        pen.color(branchColor)
        pen.lt(30)
        tree(i*branch/2)
        pen.rt(60)
        tree(i*branch/2)
        pen.left(30)
        pen.bk(i)

def run():
    tree(treeSize)

run()
turtle.done()