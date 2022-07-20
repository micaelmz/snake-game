from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=620, height=620)
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

wall_box = Turtle()
wall_box.hideturtle()
wall_box.penup()
wall_box.goto(-290, 290)
wall_box.pendown()
wall_box.pencolor('white')
wall_box.goto(290, 290)
wall_box.goto(290, -290)
wall_box.goto(-290, -290)
wall_box.goto(-290, 290)