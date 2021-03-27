import turtle

# window
win = turtle.Screen()
win.title("Abhilash pong")
win.setup(width=800, height=600)
win.bgcolor("black")
win.tracer(0)

# main menu
main = turtle.Turtle()
main.speed(0)
main.color("white")
main.penup()
main.hideturtle()
main.goto(0, 200)
main.write("PONG", align="center", font=("arial", 40, "bold"))

# AI mode
aimode = turtle.Turtle()
aimode.speed(0)
aimode.shape("square")
aimode.color("white")
aimode.shapesize(0.5, 14)
aimode.penup()
aimode.goto(0, 130)
aimode2 = turtle.Turtle()
aimode2.speed(0)
aimode2.shape("square")
aimode2.color("white")
aimode2.shapesize(0.5, 14)
aimode2.penup()
aimode2.goto(0, 80)
aimode3 = turtle.Turtle()
aimode3.speed(0)
aimode3.shape("square")
aimode3.color("white")
aimode3.shapesize(2, 0.5)
aimode3.penup()
aimode3.goto(-135, 105)
aimode4 = turtle.Turtle()
aimode4.speed(0)
aimode4.shape("square")
aimode4.color("white")
aimode4.shapesize(2, 0.5)
aimode4.penup()
aimode4.goto(135, 105)
aimodetext = turtle.Turtle()
aimodetext.speed(0)
aimodetext.color("red")
aimodetext.penup()
aimodetext.hideturtle()
aimodetext.goto(0, 80)
aimodetext.write("AI MODE", align="center", font=("courier", 30, "bold"))
# selectbutton
aimodeselectionbutton = False
if aimodeselectionbutton == True:
    aimodeselectbutton = turtle.Turtle()
    aimodeselectbutton.speed(0)
    aimodeselectbutton.shape("square")
    aimodeselectbutton.color("green")
    aimodeselectbutton.shapesize(2, 13)
    aimodeselectbutton.penup()
    aimodeselectbutton.goto(0, 105)

# Multiplayer mode
mulmode = turtle.Turtle()
mulmode.speed(0)
mulmode.shape("square")
mulmode.color("white")
mulmode.shapesize(0.5, 14)
mulmode.penup()
mulmode.goto(0, 40)
mulmode2 = turtle.Turtle()
mulmode2.speed(0)
mulmode2.shape("square")
mulmode2.color("white")
mulmode2.shapesize(0.5, 14)
mulmode2.penup()
mulmode2.goto(0, -10)
mulmode3 = turtle.Turtle()
mulmode3.speed(0)
mulmode3.shape("square")
mulmode3.color("white")
mulmode3.shapesize(2, 0.5)
mulmode3.penup()
mulmode3.goto(-135, 15)
mulmode4 = turtle.Turtle()
mulmode4.speed(0)
mulmode4.shape("square")
mulmode4.color("white")
mulmode4.shapesize(2, 0.5)
mulmode4.penup()
mulmode4.goto(135, 15)
mulmodetext = turtle.Turtle()
mulmodetext.speed(0)
mulmodetext.color("green")
mulmodetext.penup()
mulmodetext.hideturtle()
mulmodetext.goto(0, -10)
mulmodetext.write("DUAL MODE", align="center", font=("courier", 30, "bold"))
# selectbutton
mulmodeselectionbutton = False
if mulmodeselectionbutton == True:
    mulmodeselectbutton = turtle.Turtle()
    mulmodeselectbutton.speed(0)
    mulmodeselectbutton.shape("square")
    mulmodeselectbutton.color("green")
    mulmodeselectbutton.shapesize(2, 13)
    mulmodeselectbutton.penup()
    mulmodeselectbutton.goto(0, 15)

# quitbutton
quitbutton = turtle.Turtle()
quitbutton.speed(0)
quitbutton.shape("square")
quitbutton.color("white")
quitbutton.shapesize(0.5, 14)
quitbutton.penup()
quitbutton.goto(0, -55)
quitbutton2 = turtle.Turtle()
quitbutton2.speed(0)
quitbutton2.shape("square")
quitbutton2.color("white")
quitbutton2.shapesize(0.5, 14)
quitbutton2.penup()
quitbutton2.goto(0, -105)
quitbutton3 = turtle.Turtle()
quitbutton3.speed(0)
quitbutton3.shape("square")
quitbutton3.color("white")
quitbutton3.shapesize(2, 0.5)
quitbutton3.penup()
quitbutton3.goto(-135, -80)
quitbutton4 = turtle.Turtle()
quitbutton4.speed(0)
quitbutton4.shape("square")
quitbutton4.color("white")
quitbutton4.shapesize(2, 0.5)
quitbutton4.penup()
quitbutton4.goto(135, -80)
quitbuttontext = turtle.Turtle()
quitbuttontext.speed(0)
quitbuttontext.color("grey")
quitbuttontext.penup()
quitbuttontext.hideturtle()
quitbuttontext.goto(0, -100)
quitbuttontext.write("QUIT", align="center", font=("courier", 30, "bold"))
# selectbutton
quitbuttonselectionbutton = False
if quitbuttonselectionbutton == True:
    quitbuttonselectbutton = turtle.Turtle()
    quitbuttonselectbutton.speed(0)
    quitbuttonselectbutton.shape("square")
    quitbuttonselectbutton.color("grey")
    quitbuttonselectbutton.shapesize(2, 13)
    quitbuttonselectbutton.penup()
    quitbuttonselectbutton.goto(0, -80)
# selection tool
selection = "mulmode"
curzor = turtle.Turtle()
curzor.speed(0)
curzor.shape("triangle")
curzor.color("gold")
curzor.shapesize(2)
curzor.penup()
if selection == "mulmode":
    curzor.goto(160, 15)
elif selection == "aimode":
    curzor.goto(160, 105)
elif selection == "quit":
    curzor.goto(160, -80)


# game logic
def selectaimode():
    open("aimode.py", "r+")


def selectmulmode():
    open("mulmode.py", "r+")


def selectquit():
    gameover = True


option = 0


def choice():
    if option == 10:
        selectaimode()
    elif option == 20:
        selectmulmode()
    elif option == 30:
        selectquit()

def aimode():
    pass
def mulmode():
    pass
# game loop
gameover = False
ingame = True
mainmenu = True
while ingame:
    if mainmenu == True:
        win.update()
