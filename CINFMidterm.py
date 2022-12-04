#CINF 308 Midterm Project - Game Dev V2
#This is James Gillanders' Code

#For this midterm project, I will be creating a Snake clone using turtle (initially it was in pygame but I found turtle to be easier). We will have a pretty structured 
#setup here in our code, such as defining our game's appearance, adding the environment, etc. 
#I did a lot of research into turtle specifically for this project, I will include some sources I used in my pseudocode.
#We will be trying to make a basic Snake clone, keeping a minimalist design while branching out where we can. 

#All necessary libraries for this program. 
from os import environ
import turtle
import random
import time
delay = 0.1
score = 0
high_score = 0

#Defining our game environment
environment = turtle.Screen()
#Our title for the game will appear at the top of the window which we can access
#with the .title( ) function in turtle
environment.title("James' Snake Game")
#Determine a background color, in this case I want a classic black / green color palette.
environment.bgcolor("black")
#Dimensions for the game window
environment.setup(width=800, height= 800)
#.tracer() gives a light  border around the game window
environment.tracer(0)

#This alone works as when we run it a blank game window appears with the colors 
#and dimensions we specified. 

#The next section will be our snake itself, which will just be a shape on the screen.
#We have to create a "turtle", which in Python terms is something that moves around on
#the screen to put it simply. We can create a turtle with the .turtle( ) function.

#Our snake variable can be called anything but we will name our snake George.
george = turtle.Turtle()
#Defining george's speed, shape, color, and overall existence.
george.speed(0)
george.shape("square")
george.color("green")
#In turtle, we specify the thing that moves around as a "pen"
george.penup()
george.goto(0, 100)
george.direction = "stop"

#This next section will be for the fruit, the only other object in the game besides George.
fruit = turtle.Turtle()
colors = random.choice(["red", "green", "orange"])
shapes = random.choice(["square", "circle", "triangle"])
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.shapesize(0.35, 0.35)
fruit.goto(0, 100)
#Similar syntax for George's dimensions with most of the same functions.
#Defining our pen which the program is going to "write" with.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

#After running the code up to this point we get our environment with George present but we cannot move him
#or manipulate the screen in anyway. But it runs continuously, and he is on the screen so that is a good start!

#The following section will cover all movement and this is where things can get complicated.
#We have to account for directions and this involves a bit of math but it is easy once 
#we break it down.

def group():
    if george.direction != "down":
        george.direction = "up"
 
 
def godown():
    if george.direction != "up":
        george.direction = "down"
 
 
def goleft():
    if george.direction != "right":
        george.direction = "left"
 
 
def goright():
    if george.direction != "left":
        george.direction = "right"
 
 
def move():
    if george.direction == "up":
        y = george.ycor()
        george.sety(y+20)
    if george.direction == "down":
        y = george.ycor()
        george.sety(y-20)
    if george.direction == "left":
        x = george.xcor()
        george.setx(x-20)
    if george.direction == "right":
        x = george.xcor()
        george.setx(x+20)
 
#We need the system to identify which keys are being pressed, which is where the .listen( ) function comes into play.
#In simple terms, this allows the program to "hear" our commands and react accordingly. Also we need our
#key inputs to be mapped so we wil use the .onkey() function.

#The next couple of functions specify each of the directions, and if the input does not equal another, then
#George will move in the opposite one we declared.
         
environment.listen()
environment.onkeypress(group, "w")
environment.onkeypress(godown, "s")
environment.onkeypress(goleft, "a")
environment.onkeypress(goright, "d")

#We could have binded the keys to anything but I went with the traditiona WASD keybinds, which is universal
#for most games.

#Here we will add to George's body whenever a fruit is eaten, so we define a list to do this since adding data
#to it is pretty easy. 
segments = []
#Below is our main loop for events. 
while True:
    environment.update()
    if george.xcor() > 290 or george.xcor() < -290 or george.ycor() > 290 or george.ycor() < -290:
        time.sleep(1)
        george.goto(0, 0)
        george.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if george.distance(fruit) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        fruit.goto(x, y)
        #Adding a new segment to George, we specify dimensions and 
        #append another to the segment list.
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("teal")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("courier", 24, "bold"))
    #Checking for head collisions with body segments, thid will result in a game over
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = george.xcor()
        y = george.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(george) < 20:
            time.sleep(1)
            george.goto(0, 0)
            george.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("courier", 24, "bold"))
    time.sleep(delay)

environment.mainloop()