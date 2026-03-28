import turtle

from design.pieces.pawn import pawns

positions = turtle.Turtle()

def draw_at_position(x,y):
    """
    sets the turtle to a board position and draws there.
    """
    # figureing out which square
    x_cord = x//80 * 80
    y_cord = y//80 * 80
    print (x_cord,y_cord)

    # go to position
    positions.penup()
    positions.goto(x_cord, y_cord)
    positions.setheading(0)
    positions.pendown()

    # draw something at position
    pawns(positions)


    
    