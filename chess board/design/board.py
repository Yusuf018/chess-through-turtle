from design.square import construct_square

def build_board(start, t):

    for i in range(64):
        if i%8 == 0 and i!=0:
            t.penup()
            t.left(90)
            t.forward(80)
            t.left(90)
            t.forward(640)
            t.left(90)
            t.left(90)
            t.pendown()
            start=not start
        construct_square(i, start, t)
        t.penup()
        t.forward(80)
        t.pendown()

