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
    self.pu()

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
      self.setheading(0)
      self.direction = "right"
      
  def move(self):
    self.forward(20)
    if self.xcor() > 230 or self.xcor() < -230:
      self.die()
    if self.ycor() > 230 or self.ycor() < -230:
      self.die()

  def die(self):
    for g in body:
      g.ht()
    self.alive = False

      


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.color("green")
    self.shape("turtle")
    self.pu()
    self.goto(other.xcor(),other.ycor())
    self.setheading(other.heading())
    self.st()
    self.other = other
    

  def move(self):
    self.goto(self.other.xcor(),self.other.ycor())
    self.setheading(self.other.heading())
    

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.color("red")
    self.shape("square")
    self.pu()
    self.goto(random.randint(-200,200),random.randint(-200,200))
    self.showturtle()


  def relocate(self):
    self.goto(random.randint(-200,200),random.randint(-200,200))


def update():
  if head.alive == True:
    head.move()
    for i in range(len(body)-1,0,-1):
      body[i].move()
    for t in range(4,len(body)):
      if head.distance(body[t])<20:
        head.die()

    if head.distance(apple) < 20:
      apple.relocate()
      body.append(Segment(body[-1]))
    
    



    
      

    screen.ontimer(update, 120)



screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()
screen.onkey(update, "space")

playing_area()

head = Head(screen)
body = [head]
apple = Apple()
update()


screen.exitonclick()
