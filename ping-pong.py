import turtle

#Window
win = turtle.Screen()
win.title("Ping Pong by Noelle")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) 

#Paddle A
paddle_a = turtle.Turtle() #t - module, T - Class
paddle_a.speed(0) 
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #default is 20px by 20px
paddle_a.penup() 
paddle_a.goto(-350,0) #coordinates for paddle being on L side of the screen

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
#Ball Movements
Ball.dx = 0.4
Ball.dy = -0.4

#Scoring
pen = turtle.Turtle()
pen.speed(0) #animation Speed
pen.color('white')
pen.penup()
pen.hideturtle() #dont want to see the pen, just the text
pen.goto(0, 260)
pen.write("Player A: 0, Player B: 0", align="center", font =("Verdana", 24, "normal"))

#Score
score_a = 0
score_b = 0

#Functions - For moving the paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #add 20 px to y coord
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
win.listen() #listen for keyboard input
win.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up") #UpArrow
win.onkeypress(paddle_b_down, "Down") #DownArrow

#Main Game Loop
while True:
    win.update()

    #Move the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border checking - to get it to bounce, Top and Bottom Border
    if Ball.ycor() > 290: #based on height of 600(-300,300)
        Ball.sety(290)
        Ball.dy *= -1 #this reverses the direction of the ball

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    #Left and Right Border
    if Ball.xcor() > 390: #based on width of 800(-400,400), Right Side
        Ball.goto(0,0)
        Ball.dx *= -1
        #Add one if ball goes off the Screen
        score_a += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align="center", font =("Verdana", 24, "normal"))

    if Ball.xcor() < -390: #based on width of 800(-400,400)
        Ball.goto(0,0)
        Ball.dx *= -1
        #if ball goes to the left side of the Screen
        score_b += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align="center", font =("Verdana", 24, "normal"))

    #To bounce off paddles
    if (Ball.xcor() > 340 and Ball.xcor() <350) and (Ball.ycor() < paddle_b.ycor() + 50 and Ball.ycor() > paddle_b.ycor() - 50):
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340  and Ball.xcor()< -350) and (Ball.ycor() < paddle_a.ycor() + 50 and Ball.ycor() > paddle_a.ycor() - 50):
        Ball.setx(-340)
        Ball.dx *= -1
