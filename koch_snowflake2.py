import turtle

# turtle settings
turtle.speed(0)
turtle.hideturtle()

order = -10
# ask the user for order until they give a valid response
while (not type(order) == int) or (order > 0 or order < 5):
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
    elif order >= 0 and order <= 5:
        break

# initialize variables
current_order = 0
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
        line()
        turtle.right(120)

# line either draws a line or calls bump depending on the order
def line():
    if current_order < order:
        bump()
    else:
        turtle.forward(side_length)

# bump goes one level deeper
def bump():
    global current_order
    current_order += 1
    line()
    turtle.left(60)
    line()
    turtle.right(120)
    line()
    turtle.left(60)
    line()
    current_order -= 1

# Call main
main()
