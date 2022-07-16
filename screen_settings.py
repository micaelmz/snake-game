from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=620, height=620)
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

box = Turtle()
box.hideturtle()
box.penup()
box.goto(-290, 290)
box.pendown()
box.pencolor('white')
box.goto(290, 290)
box.goto(290, -290)
box.goto(-290, -290)
box.goto(-290, 290)