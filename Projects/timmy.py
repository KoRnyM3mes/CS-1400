import turtle

def main():
    relocate(0, 300, 0)
    circle("yellow", 5)
    relocate(-100, 150, 0)
    circle("black", 0.5)
    relocate(100, 150, 0)
    circle("black", 0.5)
    relocate(-50, 0, 0)
    triangle("red", 100)
    relocate(-400, -250, 0)
    square("blue", 800)
    relocate(-150, 250, 0)
    triangle("blue", 300)
    relocate(-150, -50, 0)
    rectangle("red", 300, 50)

def square(color, size):
    turtle.color(color)
    turtle.begin_fill()
    for sqrLoop in range(4):
        turtle.forward(size)
        turtle.rt(90)
    turtle.end_fill()

def relocate(x, y, rotation):
    turtle.penup()
    turtle.goto(x, y)
    turtle.rt(rotation)
    turtle.pendown()

def circle(color, diameter):
    turtle.color(color)
    turtle.begin_fill()
    count = 0
    while count < 360:
        turtle.forward(diameter)
        turtle.rt(1)
        count = count + 1
    turtle.end_fill()

def triangle(color, size):
    turtle.color(color)
    turtle.begin_fill()
    for triLoop in range(3):
        turtle.forward(size)
        turtle.lt(120)
    turtle.end_fill()

def rectangle(color, width, height):
    turtle.color(color)
    turtle.begin_fill()
    for rectLoop in range(2):
        turtle.forward(width)
        turtle.rt(90)
        turtle.forward(height)
        turtle.rt(90)
    turtle.end_fill()



if __name__ == "__main__":
    main()
    turtle.done()