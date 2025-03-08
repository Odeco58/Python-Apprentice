""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

tina = turtle.Turtle()
tina.penup()
tina.pensize(15)
tina.goto(-150,0)
tina.pendown()
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.penup()
tina.right(90)
tina.forward(80)
tina.right(90)
tina.pendown()
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(180)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.penup()
tina.right(90)
tina.forward(30)
tina.pendown()
tina.forward(50)
tina.right(90)
tina.forward(30) 
tina.right(90) 
tina.forward(50)
tina.right(90)
tina.forward(30)
tina.right(180)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.penup()
tina.forward(30)
tina.left(90)
tina.forward(50)
tina.right(180)
tina.pendown()
tina.forward(50)
tina.right(180)
tina.forward(40)
tina.right(90)
tina.forward(15)
tina.left(90)
tina.forward(10)
tina.right(90)
tina.forward(40)


tina.right(90)
tina.forward(50)


turtle.exitonclick()