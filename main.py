from turtle import Turtle, Screen
tim = Turtle()
my_screen = Screen()
my_screen.listen()
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
my_screen.onkey(key = "w", fun= move_forwards)
my_screen.onkey(key = "s", fun= move_backwards)
my_screen.onkey(key = "a", fun= turn_left)
my_screen.onkey(key = "d", fun= turn_right)
my_screen.onkey(key= "c", fun= clear_screen)



my_screen.exitonclick()