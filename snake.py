from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"




def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self,screen):
    super().__init__()
    self.alive = True
    self.speed(0)
    self.color("green")
    self.shape("turtle")
    self.direction = "right"
    screen.onkey(self.up,"w")
    screen.onkey(self.down,"s")
    screen.onkey(self.right,"d")
    screen.onkey(self.left,"a")

def up(self):
  if self.direction != "down":
    self.setheading(90)
    self.direction = "up"
def down(self):
  if self.direction != "up":
    self.setheading(-90)
    self.direction = "down"

def left(self):
  if self.direction != "right":
    self.setheading(180)
    self.direction = "left"

def right(self):
  if self.direction != "left":
    self.setheading(90)
    self.direction = "right"

def move(self):
  self.forward(5)
  if self.xcor() > 230 or self.xcor() < -230:
    self.die()
  if self.ycor() > 230 or self.ycor() < -230:
    self.die()
    
    
def die(self):
  self.ht()
  self.alive = False


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.color("green")
    self.shape("circle")
    self.pu()
    self.goto(other.xcor(),other.ycor())
    self.st()

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    pass

  def relocate(self):
    pass


def update():
  if head.alive:
    head.move()

    if head.distance(apple) < 20:
      apple.relocate()

  screen.ontimer(update, 120)



screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()
playing_area()
head = Head(screen)
screen.onkey(update, "space")

body = [head]


screen.exitonclick()






screen.exitonclick()
