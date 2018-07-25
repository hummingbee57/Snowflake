import turtle

# turtle settings
turtle.speed(0)
turtle.hideturtle()

# get the order
try:
    order = int(input("What should the order be?(0 is a triangle) "))
except:
    print("The order must be an integer.")

# make sure the order is in the right form
if order < 0:
    print("The order must be positive.")
elif order > 5:
    print("That order is too high")

# initialize variable
side_length = 500 / (3 ** order) 

def main():

    # get the turtle in position
    turtle.left(90)
    turtle.penup()
    turtle.forward(500 / (3 ** 0.5))
    turtle.pendown()
    turtle.right(150)

    # draw the base triangle
    for count in range(3):
        line(0)
        turtle.right(120)

# line either draws a line or calls bump depending on the order
def line(current_order):
    if current_order < order:
        bump(current_order + 1)
    else:
        turtle.forward(side_length)

# bump goes one level deeper
def bump(current_order):
    line(current_order)
    turtle.left(60)
    line(current_order)
    turtle.right(120)
    line(current_order)
    turtle.left(60)
    line(current_order)

# Call main
main()
