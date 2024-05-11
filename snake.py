from turtle import Turtle

class Snake:
    MOVING_DISTANCE = 20

    UP=90
    DOWN=270
    LEFT=180
    RIGHT=0

    def __init__(self):
        self.segments = []
        self.create_snake()
        #Variable for controlling heading
        self.head=self.segments[0]

    def create_snake(self):

        xcor=0
        for i in range(3):
            position = (xcor,0)
            self.add_segment(position=position)
            xcor -= 20

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #extend new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVING_DISTANCE)

    def right(self):
        if(self.head.heading()!=self.LEFT):
            self.head.setheading(self.RIGHT)

    def left(self):
        if (self.head.heading() != self.RIGHT):
            self.head.setheading(self.LEFT)

    def up(self):
        if (self.head.heading() != self.DOWN):
            self.head.setheading(self.UP)

    def down(self):
        if (self.head.heading() != self.UP):
            self.head.setheading(self.DOWN)