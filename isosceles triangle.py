import turtle
t=turtle.Turtle()
turtle.bgcolor("violet")        
t.color("blue")
t.pensize(5)                

t.forward(400)
t.left(140)
t.forward(260)
t.up()
t.goto(0,0)
t.down()
t.setheading(40)
t.fd(260)
t.hideturtle()


turtle.exitonclick()            # wait for a user click on the canvas
