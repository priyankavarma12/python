#Circle of Squares
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
#Circles in Squares
def square(n, angle):
  for i in range(4):   
    my_turtle.forward(n)
    my_turtle.right(angle)
    my_turtle.color("blue")

for i in range(100):
    square(100,90)
    my_turtle.left(11) # we are making the 36 rotation , check prime number to get more denser circle
    my_turtle.color("green")
#square(150)
#square(50)
 

# Circle has 360 degrees
# 360/10 --> 36


