import turtle , math , random , winsound

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space_invaders_background.gif")


screen.register_shape("invader.gif")
screen.register_shape("player.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score=0

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring= "Score %s" %score
score_pen.write(scorestring,False , align="left", font=("Arial", 13, "normal"))
score_pen.hideturtle()

player=turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerSPEED= 15


enmeySPEED = 1

num_of_enemies = 5
enmeys = []
for i in range(num_of_enemies):
    enmeys.append(turtle.Turtle())
    for enmey in enmeys :

     enmey.color("red")
     enmey.shape("invader.gif")
     enmey.penup()
     enmey.speed(0)
     x=random.randint(-200,200)
     y=random.randint(100,250)
     enmey.setposition(x, y)
    enmeySPEED = 7

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletSPEED= 30

bulletsteate = "ready"


def move_left():
    x=player.xcor()
    x-=playerSPEED
    if x < -280 :
        x = -280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerSPEED
    if x > 280 :
        x= 280
    player.setx(x)

def  isCollision (t1 ,t2 ) :
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    if distance < 15 :

     return True

    else:
        return False



def fire_bullet ():
    global bulletsteate
    if bulletsteate == "ready":

        bulletsteate ="fire"
        x= player.xcor()
        y= player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        winsound.PlaySound("LASRFIR2", winsound.SND_ASYNC)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet,"space")
while True :
    for enmey in enmeys:
      x = enmey.xcor()
      x += enmeySPEED
      enmey.setx(x)
      if enmey.xcor() > 280:
         for e in enmeys :
          y = e.ycor()
          y -= 40
          e.sety(y)
         enmeySPEED *= -1

      if enmey.xcor() < -280:
         for e in  enmeys:
          y = e.ycor()
          y -= 40

          e.sety(y)
          enmeySPEED *= -1


      if isCollision(bullet, enmey):
             winsound.PlaySound("explosion", winsound.SND_ASYNC)
             bullet.hideturtle()
             bulletsteate = "ready"
             bullet.setposition(0, -400)
             x = random.randint(-200, 200)
             y = random.randint(100, 250)
             enmey.setposition(x, y)
             score+=10
             scorestring="Score: %s" %score
             score_pen.clear()
             score_pen.write(scorestring, False, align="left", font=("Arial", 13, "normal"))

      if isCollision(player, enmey):
             winsound.PlaySound("explosion", winsound.SND_ASYNC)
             player.hideturtle()
             enmey.hideturtle()
             print("Game Over")



    if bulletsteate == "fire":
         y = bullet.ycor()
         y += bulletSPEED
         bullet.sety(y)

    if bullet.ycor() > 280:
         bullet.hideturtle()
         bulletsteate = "ready"
         






        






