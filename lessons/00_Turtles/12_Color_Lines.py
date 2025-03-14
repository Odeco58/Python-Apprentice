"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.pensize(9)
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
forward = 50
right = 90
color = ['red', 'black', 'orange', 'blue']
for item in color:
    tina.color(item)
    tina.forward(forward)
    tina.right(right)


turtle.exitonclick()                     # Close the window when we click on it