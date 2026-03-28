from initial_constants import palette, palette_name

def empty_square(t):
    for i in range(4):
        t.forward(80)
        t.left(90)

def filled_square(t):
    t.begin_fill()
    t.fillcolor(palette[palette_name][0])
    empty_square(t)
    t.end_fill()


def construct_square(i,start,t):
    if start:
        if i%2 == 0:
            filled_square(t)
        elif i%2 != 0:
            t.fillcolor(palette[palette_name][1])
            t.begin_fill()
            empty_square(t)
            t.end_fill()
    else:
        if i%2 != 0:
            filled_square(t)
        elif i%2 == 0:
            t.fillcolor(palette[palette_name][1])
            t.begin_fill()
            empty_square(t)
            t.end_fill()
