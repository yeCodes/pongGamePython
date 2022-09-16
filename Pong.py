
import turtle # library/ MODULE
# basic graphics - builtt in lib
# pyGame also a graphics lib

# Setting up GAME ENVIRONMENT
wn = turtle.Screen()
wn.title("Pong by Y")
wn.bgcolor("black")

wn.setup(width=800, height=600)
# stop window from updating. manual update required
wn.tracer(0)

# Score varables
score_a = 0
score_b = 0


# Paddle A = define CENTRE of paddle
#turtle == MODULE
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# drawing?
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # as objects draw lines as they move otherwise
paddle_a.goto(-350,0)

# Paddle B == define CENTRE of paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # as objects draw lines as they move otherwise
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # as objects draw lines as they move otherwise
ball.goto(0,0)

# ball update
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)	# animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align = "center", font = ("Courier",24,"normal"))
pen.hideturtle()
# function 
def paddle_a_up():
    #ycor from turt module
    y = paddle_a.ycor()
    y += 20 # add 20 pixels to y
    paddle_a.sety(y)   # no return here

def paddle_a_down():
    #ycor from turt module
    y = paddle_a.ycor()
    y -= 20 # add 20 pixels to y
    paddle_a.sety(y)   # no return here

# function 
def paddle_b_up():
    #ycor from turt module
    y = paddle_b.ycor()
    y += 20 # add 20 pixels to y
    paddle_b.sety(y)   # no return here

def paddle_b_down():
    #ycor from turt module
    y = paddle_b.ycor()
    y -= 20 # add 20 pixels to y
    paddle_b.sety(y)   # no return here

# keyboard binding - events + event handling
wn.listen()     # window listens for keyboard inputs
wn.onkeypress(paddle_a_up,"w")      #when user presses w, run paddle up
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")      #when user presses w, run paddle up
wn.onkeypress(paddle_b_down,"Down")
# Main game loop
while True:
    wn.update()     #so continually update screen while window open

    # This executes whenever condition is true
    # If used explicit OOP, would call ball position + update that directly using methods
    # this is what happens here

    # Move the ball up
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    # check y top border
    if ball.ycor() > 290:		
        ball.sety(290)
        ball.dy *= -1  # move ball down. updates the dy defined outside main

    #Border checkingwww
    # check y bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #ball.sety(290)     # set ball to top, then move down
        #ball.dy *= 1  # move ball down. updates the dy defined outside main

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align = "center", font = ("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align = "center", font = ("Courier",24,"normal"))
	
	# check if paddle at y limit    
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_a.ycor() >250:
	    paddle_a.sety(250)
	    
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    if paddle_b.ycor() >250:
	    paddle_b.sety(250)

        # Paddle and ball collisions
 
    # if x cor == plane which paddle border on AND if ycor == same as ycor of paddle centre +/- height
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and  ball.ycor() > paddle_b.ycor() -40):
        #if ball lies somewhere on RHS paddle and y.cor lies between the paddle's top and bottom
        # could have structured as 3-layer nested for loop
        ball.setx(340)  #place on boundary
        ball.dx *= -1       # reverse x direction of ball
   
    if (ball.xcor() <= -340) and (ball.ycor() < paddle_a.ycor() +40 and  ball.ycor() > paddle_a.ycor() -40):
        # if ball lies somewhere on LHS paddle and y.cor lies between the paddle's top and bottom
        # could have structured as 3-layer nested for loop
        ball.setx(-340)  #place on boundary
        ball.dx *= -1       # reverse x direction of ball
    