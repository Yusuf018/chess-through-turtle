import turtle
from initial_constants import initial
from interaction.click import screen_click
from design.board import build_board
from design.build_pieces import build_pieces

t = turtle.Turtle()
s = turtle.Screen()
s.setworldcoordinates(0, 0, 650, 650)
turtle.tracer(0,0)    
t.speed(10)
start = False

def main():
    build_board(start,t)
    build_pieces(initial, flipped=True)
    s.onclick(screen_click)
    turtle.update()
    t.hideturtle()
    
if __name__ == "__main__":
    main()
turtle.done()
    
