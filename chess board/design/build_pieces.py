import turtle
from initial_constants import palette, palette_name
from design.pieces.bishop import bishops
from design.pieces.king import kings
from design.pieces.knight import knights
from design.pieces.pawn import pawns
from design.pieces.queen import queens
from design.pieces.rook import rooks

initial_setup = turtle.Turtle()
highlight_setup = turtle.Turtle()
SQUARE_SIZE = 80
BOARD_SIZE = 8


def get_screen_coords(position, flipped=False):
    file_no = position // 10
    rank_no = position % 10

    if flipped:
        draw_x = (BOARD_SIZE - file_no) * SQUARE_SIZE
        draw_y = (BOARD_SIZE - rank_no) * SQUARE_SIZE
    else:
        draw_x = (file_no - 1) * SQUARE_SIZE
        draw_y = (rank_no - 1) * SQUARE_SIZE

    return draw_x, draw_y


def build_pieces(initial, flipped=False):
    for i in initial:
        draw_x, draw_y = get_screen_coords(i, flipped)
        initial_setup.penup()
        initial_setup.goto(draw_x, draw_y)
        initial_setup.setheading(0)
        initial_setup.pendown()

        if initial[i] and initial[i][0] == "w":
            initial_setup.color(palette[palette_name][3])
        else:
            initial_setup.color(palette[palette_name][2])

        if initial[i] and initial[i][1:-1] == "pawn":
            pawns(initial_setup)
        if initial[i] and initial[i][1:-1] == "rook":
            rooks(initial_setup)
        if initial[i] and initial[i][1:-1] == "bishop":
            bishops(initial_setup)
        if initial[i] and initial[i][1:-1] == "knight":
            knights(initial_setup)
        if initial[i] and initial[i][1:] == "queen":
            queens(initial_setup)
        if initial[i] and initial[i][1:] == "king":
            kings(initial_setup)

    initial_setup.hideturtle()
    turtle.update()


def clear_highlights():
    highlight_setup.clear()


def highlight_squares(positions, flipped=False, color="#3FA34D"):
    highlight_setup.penup()
    highlight_setup.pensize(3)
    highlight_setup.pencolor(color)

    for pos in positions:
        draw_x, draw_y = get_screen_coords(pos, flipped)

        # Draw a clear inset border around legal destination squares.
        highlight_setup.goto(draw_x + 4, draw_y + 4)
        highlight_setup.setheading(0)
        highlight_setup.pendown()
        for _ in range(4):
            highlight_setup.forward(72)
            highlight_setup.left(90)
        highlight_setup.penup()

    highlight_setup.hideturtle()
    turtle.update()
