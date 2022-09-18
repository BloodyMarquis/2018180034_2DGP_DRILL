import turtle

count1 = 6
count2 = 6

turtle.left(90)
while (count1 > 0) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100*(7 - count1), 0)
    count1 -= 1

turtle.home()
while (count2 > 0) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0, 100*(7 - count2))
    count2 -= 1

turtle.exitonclick()
