import turtle
turtle.setup(width = 600, height = 600)

tina= turtle.Turtle()
tina.color("red")
tina.speed(-1)
for i in range(450):
    tina.color("green")

    tina.forward(64) 

    tina.left(90) 

    tina.forward(89) 

    tina.color("red")

    tina.right(500) 

    tina.forward(89) 

    tina.color("blue")

    tina.right(62) 

    tina.forward(89)

tina.hideturtle() 
    
turtle.exitonclick()