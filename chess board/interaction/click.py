import turtle

from initial_constants import initial
from design.build_pieces import build_pieces, initial_setup, clear_highlights, highlight_squares
from interaction.move_validation.check_valid import valid_move, get_legal_moves, get_game_state

selecting = False
selected = ""
selected_position = None
selected_moves = []
current_turn = "w"
game_over = False
board_flipped = current_turn == "w"

status_writer = turtle.Turtle()
status_writer.hideturtle()
status_writer.penup()
status_writer.goto(320, 620)


def turn_name(color):
    return "White" if color == "w" else "Black"


def board_flipped_for_turn(color):
    return color == "w"


def write_status(message):
    status_writer.clear()
    status_writer.color("#111111")
    status_writer.write(message, align="center", font=("Arial", 14, "bold"))


def screen_click(x, y):
    global selecting
    global selected
    global selected_position
    global selected_moves
    global current_turn
    global game_over
    global board_flipped

    initial_setup.clear()
    clear_highlights()

    # Ignore clicks after game is over.
    if game_over:
        build_pieces(initial, board_flipped)
        return

    x_square = int(x // 80) + 1
    y_square = int(y // 80) + 1

    # Bounds guard for clicks outside the 8x8 board.
    if not (1 <= x_square <= 8 and 1 <= y_square <= 8):
        build_pieces(initial, board_flipped)
        if selecting:
            highlight_squares(selected_moves, board_flipped)
        return

    if board_flipped:
        file_no = 9 - x_square
        rank_no = 9 - y_square
    else:
        file_no = x_square
        rank_no = y_square

    position = file_no * 10 + rank_no
    piece = initial[position]

    if not selecting:
        if piece is None:
            write_status(f"{turn_name(current_turn)} to move")
        elif piece[0] != current_turn:
            write_status(f"{turn_name(current_turn)} to move")
        else:
            selecting = True
            selected = piece
            selected_position = position
            selected_moves = get_legal_moves(initial, selected, selected_position)
            write_status(f"{turn_name(current_turn)} selected {selected}")
    else:
        # Clicking the same square deselects.
        if position == selected_position:
            selecting = False
            selected = ""
            selected_position = None
            selected_moves = []
            write_status(f"{turn_name(current_turn)} to move")

        # Allow reselection of another piece from the same side.
        elif piece is not None and piece[0] == current_turn:
            selected = piece
            selected_position = position
            selected_moves = get_legal_moves(initial, selected, selected_position)
            write_status(f"{turn_name(current_turn)} selected {selected}")

        else:
            moved = valid_move(initial, selected, selected_position, piece, position)
            if moved:
                initial[position] = selected
                initial[selected_position] = None

                selecting = False
                selected = ""
                selected_position = None
                selected_moves = []

                current_turn = "b" if current_turn == "w" else "w"
                board_flipped = board_flipped_for_turn(current_turn)
                game_state = get_game_state(initial, current_turn)

                if game_state["state"] == "normal":
                    write_status(f"{turn_name(current_turn)} to move")
                elif game_state["state"] == "check":
                    write_status(f"Check on {turn_name(current_turn)}")
                elif game_state["state"] == "checkmate":
                    game_over = True
                    write_status(f"Checkmate! {turn_name(game_state['winner'])} wins")
                elif game_state["state"] == "stalemate":
                    game_over = True
                    write_status("Stalemate! Draw")
            else:
                # Keep selection active so user can try another destination.
                selected_moves = get_legal_moves(initial, selected, selected_position)
                write_status("Invalid move")

    build_pieces(initial, board_flipped)
    if selecting:
        highlight_squares(selected_moves, board_flipped)


write_status("White to move")
