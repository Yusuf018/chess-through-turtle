def valid_move(initial, selected, selected_position, move_to, move_to_position):
    legal_moves = get_legal_moves(initial, selected, selected_position)
    if move_to_position not in legal_moves:
        print("invalid move")
        return False
    return True


def get_legal_moves(initial, selected, selected_position):
    pseudo_moves = construct_valid_list(initial, selected, selected_position, for_attack=False)
    legal_moves = []

    for move in pseudo_moves:
        if move not in initial:
            continue

        target_piece = initial[move]
        if is_same_color(target_piece, selected):
            continue

        temp_board = initial.copy()
        temp_board[move] = selected
        temp_board[selected_position] = None

        if not is_in_check(temp_board, selected[0]):
            legal_moves.append(move)

    return legal_moves


def construct_valid_list(initial, selected, selected_position, move_to=None, move_to_position=None, for_attack=False):
    valid_moves = []
    piece_type = get_piece_type(selected)

    if piece_type == "pawn":
        if selected[0] == "b":
            forward_one = selected_position + 1
            forward_two = selected_position + 2
            capture_left = selected_position - 9
            capture_right = selected_position + 11
            start_rank = 2
        else:
            forward_one = selected_position - 1
            forward_two = selected_position - 2
            capture_left = selected_position - 11
            capture_right = selected_position + 9
            start_rank = 7

        if for_attack:
            for capture in (capture_left, capture_right):
                if capture in initial:
                    valid_moves.append(capture)
            return valid_moves

        if forward_one in initial and initial[forward_one] is None:
            valid_moves.append(forward_one)

            # Two-square pawn push requires both squares to be clear.
            if selected_position % 10 == start_rank and forward_two in initial and initial[forward_two] is None:
                valid_moves.append(forward_two)

        for capture in (capture_left, capture_right):
            if capture in initial and initial[capture] is not None and not is_same_color(initial[capture], selected):
                valid_moves.append(capture)

        return valid_moves

    if piece_type == "knight":
        deltas = [12, -8, -12, 8, 21, -21, 19, -19]
        for delta in deltas:
            pos = selected_position + delta
            if pos in initial and not is_same_color(initial[pos], selected):
                valid_moves.append(pos)
        return valid_moves

    if piece_type == "rook":
        valid_moves.extend(_line_moves(initial, selected, selected_position, [(-1, 0), (1, 0), (0, -1), (0, 1)]))
        return valid_moves

    if piece_type == "bishop":
        valid_moves.extend(_line_moves(initial, selected, selected_position, [(-1, -1), (-1, 1), (1, -1), (1, 1)]))
        return valid_moves

    if piece_type == "queen":
        # Queen should stop on first blocker in every direction.
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1),
        ]
        valid_moves.extend(_line_moves(initial, selected, selected_position, directions))
        return valid_moves

    if piece_type == "king":
        deltas = [1, -1, 10, -10, 11, -11, 9, -9]
        for delta in deltas:
            pos = selected_position + delta
            if pos in initial and not is_same_color(initial[pos], selected):
                valid_moves.append(pos)
        return valid_moves

    return valid_moves


def _line_moves(initial, selected, selected_position, directions):
    moves = []
    start_x = selected_position // 10
    start_y = selected_position % 10

    for dx, dy in directions:
        x = start_x + dx
        y = start_y + dy

        while 1 <= x <= 8 and 1 <= y <= 8:
            pos = x * 10 + y
            piece = initial[pos]

            if piece is None:
                moves.append(pos)
            else:
                if not is_same_color(piece, selected):
                    moves.append(pos)
                break

            x += dx
            y += dy

    return moves


def is_in_check(initial, color):
    king_position = find_king_position(initial, color)
    if king_position is None:
        return False

    enemy_color = "b" if color == "w" else "w"
    return is_square_attacked(initial, king_position, enemy_color)


def is_square_attacked(initial, square, by_color):
    for position, piece in initial.items():
        if piece is None or piece[0] != by_color:
            continue

        attacks = construct_valid_list(initial, piece, position, for_attack=True)
        if square in attacks:
            return True

    return False


def find_king_position(initial, color):
    for position, piece in initial.items():
        if piece and piece[0] == color and get_piece_type(piece) == "king":
            return position
    return None


def has_any_legal_moves(initial, color):
    for position, piece in initial.items():
        if piece and piece[0] == color:
            if get_legal_moves(initial, piece, position):
                return True
    return False


def get_game_state(initial, color_to_move):
    in_check = is_in_check(initial, color_to_move)
    has_moves = has_any_legal_moves(initial, color_to_move)

    if has_moves:
        if in_check:
            return {"state": "check", "winner": None}
        return {"state": "normal", "winner": None}

    if in_check:
        winner = "b" if color_to_move == "w" else "w"
        return {"state": "checkmate", "winner": winner}

    return {"state": "stalemate", "winner": None}


def get_piece_type(piece):
    return piece[1:].rstrip("0123456789")


def is_same_color(move_to, selected):
    if move_to and selected[0] == move_to[0]:
        return True
    return False
