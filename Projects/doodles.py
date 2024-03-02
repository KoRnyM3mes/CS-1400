'''
docstring
'''

#import modules
import turtle
import sys
# Function to draw shapes
def draw(selection):
    turtle.speed(0)
    draw_scene(selection)

def draw_scene(selection):
    if selection == 1:
        skinColor = "yellow"
        eyeColor = "blue"
        clothColor = "red"
    else:
        skinColor = "green"
        eyeColor = "red"
        clothColor = "black"

    face(skinColor, eyeColor, clothColor)

def face(skinColor, eyeColor, clothColor):
    relocate(0, 300, 0)
    circle(skinColor, 5)
    eyeball(eyeColor, 1, -100, 200, 175, 165)
    eyeball(eyeColor, 1, 100, 200, 175, 165)
    relocate(-50, 0, 0)
    triangle("red", 100)
    relocate(-400, -250, 0)
    square(clothColor, 800)
    relocate(-150, 250, 0)
    triangle(clothColor, 300)
    relocate(-150, -50, 0)
    rectangle("red", 300, 50)

def eyeball(color, size, x, y, y1, y2):
    relocate(x, y, 0)
    circle("white", size)
    relocate(x, y1, 0)
    circle(color, size / 2)
    relocate(x, y2, 0)
    circle("black", size / 4)

def relocate(x, y, rotation):
    turtle.penup()
    turtle.goto(x, y)
    turtle.rt(rotation)
    turtle.pendown()

def square(color, size):
    turtle.color(color)
    turtle.begin_fill()
    for sqrLoop in range(4):
        turtle.forward(size)
        turtle.rt(90)
    turtle.end_fill()

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
        
# Main function
def main():
    try:
        selection = int(sys.argv[1])
    except:
        print("Usage: doodles.py <selection> where selection must be one of 1 or 2")
        return
    if selection not in (1, 2):
        print("Usage: doodles.py <selection> where selection must be one of 1 or 2")
        return
    draw(selection)
    turtle.done

# program kicks off here -- must call turtle.done() AFTER main().
if __name__ == "__main__":
    main()
    turtle.done()