"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window

t = ... # Create a turtle named t



# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    ...

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

import turtle

t = turtle.Turtle()

t.shape("turtle")

t.width(2) 

t.speed(0) 

for i in range(40):
    
    t.width(2) 

    t.speed(0) 
   
    t.pencolor("red")

    t.forward(200) 

    t.left(90) 

    t.forward(64) 

    t.right(200) 

    t.forward(64) 

    t.right(62) 

    t.forward(200) 

t.hideturtle() 

turtle.exit_on_click()

 
