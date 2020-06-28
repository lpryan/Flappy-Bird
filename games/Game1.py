import turtle, time,random

Flappy_Bird_up = "Flappy Down.gif"
Flappy_Bird_down = "Flappy Up.gif"
Flappy_Bird = "Flappy.gif"
Pipe_Top = "Pipe Top.gif"
Pipe_Bottom = "Pipe Bottom.gif"
Play_Button = "Play-Button.gif"

turtle.hideturtle()
turtle.addshape(Flappy_Bird)
turtle.addshape(Flappy_Bird_down)
turtle.addshape(Flappy_Bird_up)
turtle.addshape(Pipe_Top)
turtle.addshape(Pipe_Bottom)
turtle.addshape(Play_Button)

turtle.shape("square")
turtle.color("#5cb3ce")
turtle.setx(700)
Flappy = turtle.Turtle()

Pipe_Top_Turtle = Flappy.clone()
Pipe_Bottom_Turtle = Flappy.clone()
Score_Counter = Flappy.clone()
Play_button_turtle = Flappy.clone()

Play_button_turtle.sety(0)
Play_button_turtle.setx(0)

Pipe_Top_Turtle.shape(Pipe_Top)
Pipe_Bottom_Turtle.shape(Pipe_Bottom)
Flappy.shape(Flappy_Bird)
Play_button_turtle.shape(Play_Button)
print "hello"

turtle.screensize(640, 540)
turtle.bgpic("Background.gif")
turtle.showturtle()


Flappy.penup()
Pipe_Bottom_Turtle.penup()
Pipe_Top_Turtle.penup()
Score_Counter.penup()


Flappy.sety(0)
Pipe_Bottom_Turtle.speed(0)
Pipe_Top_Turtle.speed(0)

Flappy.setx(-200)
Pipe_Top_Turtle.setx(300)
Pipe_Bottom_Turtle.setx(300)

Score_Counter.hideturtle()

Score_Counter.setx(-210)
Score_Counter.sety(260)
Score_Counter.speed(0)

current_time_sec = list(time.gmtime())[5]
global Obstacles
Obstacles = False
global Start
Start = True
global score
score = 0
global previous_print
previous_print = 0
global PipeNumber
PipeNumber = 1
global Highscore
Previous_Scores = open("Highscores","r")
global speed
speed = 0



Highscore = max([int(i.split("\n")[0]) for i in Previous_Scores.readlines( )])


Score_Counter.write("Score: " + str(score) + " High: " + str(Highscore) , True, align="center",font=("Arial", 20, "bold"))



def Jump():
    ground = -175
    gravity = .98
    force = 10
    force += gravity
    while True:
        global Obstacles
        global Start
        if Start == True:
            height = random.randint(-60, 60)
            Pipe_Top_Turtle.sety(height + 460)
            Pipe_Bottom_Turtle.sety(height - 460)
            speed += 10
            Obstacles = True
            Start = False
        if Obstacles == False:
            height = random.randint(-60,60)
            Pipe_Top_Turtle.sety(height + 460)
            Pipe_Bottom_Turtle.sety(height - 460)
            Obstacles = True
        else:
            global score
            global speed
            Pipe_Top_Turtle.setx(Pipe_Top_Turtle.xcor() - speed)
            Pipe_Bottom_Turtle.setx(Pipe_Bottom_Turtle.xcor() - speed)
            if Pipe_Bottom_Turtle.xcor() <= -320:
                Pipe_Top_Turtle.setx(300)
                Pipe_Bottom_Turtle.setx(300)
                global PipeNumber
                PipeNumber += 1
                Obstacles = False
                if score % 5 == 0:
                    speed += 5
        global score
        global previous_print

        if previous_print != score:
            Score_Counter.clear()
            Score_Counter.setx(-210)
            Score_Counter.sety(260)
            Score_Counter.write("Score: " + str(score) + " High: " + str(Highscore) , True, align="center",font=("Arial", 20, "bold"))
            previous_print = score

        force -= gravity
        if force < 0:
            Flappy.settiltangle(-45)
            Flappy.shape(Flappy_Bird_up)
        elif force > 0:
            Flappy.settiltangle(45)
            Flappy.shape(Flappy_Bird_down)
        else:
            Flappy.settiltangle(0)
            Flappy.shape(Flappy_Bird)
        global PipeNumber
        if abs(Flappy.xcor() - Pipe_Bottom_Turtle.xcor()) < 40:
            global score
            if PipeNumber > score:
                score += 1
            elif PipeNumber <= score:
                score = PipeNumber


        if Flappy.ycor() + force <= ground:
            Flappy.sety(ground)
            force = 0
            break
        if abs(Flappy.ycor() - Pipe_Top_Turtle.ycor()) < 396.5 and abs(Flappy.xcor() - Pipe_Top_Turtle.xcor()) < 69:
            break
        if abs(Flappy.ycor() - Pipe_Bottom_Turtle.ycor()) < 396.5 and abs(Flappy.xcor() - Pipe_Bottom_Turtle.xcor()) < 69:
            break
        Flappy.sety(Flappy.ycor() + force)
    Flappy.stamp()
    Flappy.hideturtle()
    Flappy.setpos(0,0)
    Flappy.write("Game Over", True, align="center",font=("Arial", 20, "bold"))
    Scores = open("Highscores","a")
    Scores.write(str(score)+"\n")
    turtle.done()

def Release():
    Play_button_turtle.onrelease(Begin())
def Begin(x,y):
    Play_button_turtle.hideturtle()
    Play_button_turtle.penup()
    turtle.bgpic("Background.gif")
    Pipe_Bottom_Turtle.showturtle()
    Pipe_Top_Turtle.showturtle()
    Flappy.showturtle()


    for i in range(4):
        Play_button_turtle.clear()
        Play_button_turtle.write(3-i, True, align="center",font=("Arial", 30, "bold"))
        time.sleep(1)
        Play_button_turtle.setx(0)
        Play_button_turtle.sety(0)
    Play_button_turtle.clear()

    print "Start"
    turtle.onkey(Jump,"space")
    turtle.listen()
    turtle.onkey(turtle.done,"z")
    turtle.mainloop()
canvas = turtle.getcanvas()
mouseX, mouseY = canvas.winfo_pointerx(), canvas.winfo_pointery()

turtle.bgpic("Starting-Background.gif")
Pipe_Bottom_Turtle.hideturtle()
Pipe_Top_Turtle.hideturtle()
Flappy.hideturtle()



for i in range(1):
    Play_button_turtle.onclick(Begin)
    turtle.listen()
    turtle.mainloop()
print "Exit"