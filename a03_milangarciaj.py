#################################################################################
# Author: Milan Garcia
# Username: milangarciaj
#
# Assignment: A03
# Google Doc Link: https://docs.google.com/document/d/1JZEAl2ab7GlI-5XixYCuo47_O_98IuEH-wEFNZzHb94/edit?usp=sharing
#
#################################################################################

import turtle                   # allows us to use the turtles library


def create_roof(shape):
    '''
    Create the roof of the house
    :param shape: Turtle object
    :return: None
    '''
    shape.penup()
    shape.setpos(-200, -70)
    shape.pendown()
    shape.color(252, 3, 107)
    shape.begin_fill()
    for side in range(3):
        shape.forward(150)
        shape.left(120)
    shape.end_fill()

#lol
#lol 2
#2
def create_main_house(shape):
    '''
    Creates the main house rectangle
    :param shape: Turtle object
    :return: None
    '''
    shape.setpos(-200, -70)
    shape.color(39, 214, 103)
    shape.begin_fill()
    for side in range(2):
        shape.forward(150)
        shape.right(90)
        shape.forward(180)
        shape.right(90)
    shape.end_fill()


def create_window(shape, x, y):
    '''
    Adds a window to the house
    :param shape: Turtle object
    :param x: The X coordinate of the window
    :param y: The Y coordinate of the window
    :return: None
    '''
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color(39, 182, 214)
    shape.begin_fill()
    for side in range(2):
        shape.forward(45)
        shape.right(90)
        shape.forward(35)
        shape.right(90)
    shape.end_fill()


def create_door(shape):
    '''
    Adds a door to the house
    :param shape: Turtle object
    :return: None
    '''
    shape.penup()
    shape.setpos(-145, -180)
    shape.pendown()
    shape.color(39, 182, 214)
    shape.begin_fill()
    for side in range(2):
        shape.forward(40)
        shape.right(90)
        shape.forward(70)
        shape.right(90)
    shape.end_fill()


def create_house(wn, shape):
    '''
    Adds a house right next to the house we created
    :param wn: Turtle Screen object
    :param shape: Turtle object
    :return: None
    '''
    wn.register_shape("house_2.gif")    # Registers a shape, so it can be used by the turtle library
    shape.penup()
    shape.setpos(125, -150)
    shape.shape("house_2.gif")          # Sets the shape to the image registered above
    shape.stamp()
    shape.up()


def make_text(shape, txt):
    '''
    Writes text to the screen
    :param shape: Turtle object
    :param txt: Text that will appear on the screen
    :return: None
    '''
    shape.color(237, 14, 14)
    shape.setpos(10, 110)
    shape.write(txt, move=False, align='center', font=("Arial", 40, ("bold", "normal")))


def main():
    '''
    Draws a house at x,y on the screen
    :return:None
    '''
    turtle.colormode(255)           # change color modes

    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("country.gif")         # Sets a country background
    shape = turtle.Turtle()
    shape.hideturtle()

    # Function calls for each part of the house
    create_roof(shape)
    create_main_house(shape)
    create_window(shape, -180, -110)
    create_window(shape, -115, -110)
    create_door(shape)
    create_house(wn, shape)
    make_text(shape, "Milan's country house")

    wn.exitonclick()                # Closes the program when a user clicks in the window


main()                              # call main()
