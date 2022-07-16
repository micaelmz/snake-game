from turtle import Turtle

START_POSITION = [(0, 0), (-15, 0), (-30, 0), (-45, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle()
        new_segment.shapesize(0.75, 0.75)
        new_segment.color('dark olive green')
        new_segment.penup()
        new_segment.goto(pos)
        new_segment.shape('square')
        if pos == START_POSITION[1]:
            new_segment.shape('circle')
            new_segment.shapesize(1.2, 1.2)
        if pos == START_POSITION[0]:
            new_segment.shape('circle')
            new_segment.shapesize(0.3, 0.3)
            new_segment.color('red')
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
