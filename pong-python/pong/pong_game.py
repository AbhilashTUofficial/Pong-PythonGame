import turtle
import winsound

#window
win=turtle.Screen()
win.title("Abhilash pong")
win.setup(width=800,height=600)
win.bgcolor("black")
win.tracer(0)

#paddle A
paddle_A=turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#paddle B
paddle_B=turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=.2
ball.dy=.2



#score
score_a=0
score_b=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player A: 0  player B: 0",align="center",font=("courier", 14,"normal"))

#game logic
def paddle_A_up():
    y=paddle_A.ycor()
    y+=20
    paddle_A.sety(y)
def paddle_A_down():
    y=paddle_A.ycor()
    y-=20
    paddle_A.sety(y)
def paddle_B_up():
    y=paddle_B.ycor()
    y+=20
    paddle_B.sety(y)
def paddle_B_down():
    y=paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_A_up , "w")
win.onkeypress(paddle_A_down , "s")
win.onkeypress(paddle_B_up , "o")
win.onkeypress(paddle_B_down , "l")


#gameloop
while True:
     win.update()
     #moment of ball
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)
     #border hit
     if ball.ycor() > 290:
         ball.sety(290)
         ball.dy *= -1
         winsound.PlaySound("ping.wav",winsound.SND_ASYNC)

     if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy *= -1
         winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

     if ball.xcor()>390:
         ball.goto(0,0)
         ball.dx*=-1
         score_a+=1
         score.clear()
         score.write("player A: {}  player B: {}".format(score_a,score_b), align="center", font=("courier", 14, "normal"))

     if ball.xcor()<-390:
         ball.goto(0,0)
         ball.dx*=-1
         score_b+=1
         score.clear()
         score.write("player A: {}  player B: {}".format(score_a,score_b), align="center", font=("courier", 14, "normal"))

     #paddle hit
     if (ball.xcor()> 340and ball.xcor()< 350)and(ball.ycor()<paddle_B.ycor()+40 and ball.ycor()>paddle_B.ycor()-40):
         ball.setx(340)
         ball.dx*=-1

     if (ball.xcor()<-340and ball.xcor()>-350)and(ball.ycor()>paddle_A.ycor()-40 and ball.ycor()<paddle_A.ycor()+40):
         ball.setx(-340)
         ball.dx*=-1
