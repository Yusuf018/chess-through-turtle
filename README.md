# chess-through-turtle
a fully playable chess game made solely using turtle.
# Chess Board

A Python chess game built with the standard-library `turtle` module. The project draws a full 8x8 board, renders custom piece shapes, supports click-to-select movement, highlights legal moves, alternates turns automatically, and detects check, checkmate, and stalemate.

This is a local desktop game rather than a web app or engine package, so you can run it directly with Python and play by clicking the board.

## Features

- Graphical chess board drawn with `turtle`
- Custom-drawn chess pieces
- Click-based piece selection and movement
- Legal move highlighting for the selected piece
- Turn-based play for White and Black
- Automatic board flipping after each move
- Move validation that prevents moving into check
- Detection for:
  - check
  - checkmate
  - stalemate
- Configurable color palettes for the board and pieces

## Tech Stack

- Python 3
- Standard-library `turtle`

No third-party packages are required based on the current codebase.

## Project Structure

```text
chess board/
|-- main.py
|-- initial_constants.py
|-- board_position/
|   `-- positions.py
|-- design/
|   |-- board.py
|   |-- build_pieces.py
|   |-- square.py
|   `-- pieces/
|       |-- bishop.py
|       |-- king.py
|       |-- knight.py
|       |-- pawn.py
|       |-- queen.py
|       `-- rook.py
|-- interaction/
|   |-- click.py
|   `-- move_validation/
|       `-- check_valid.py
`-- movement/
    |-- pawns.py
    `-- test.py
```

## How It Works

### Entry Point

`main.py` sets up the `turtle` screen, draws the board, places all pieces in their initial positions, and registers the mouse click handler.

### Board Representation

The board is stored as a dictionary in `initial_constants.py`. Keys are numeric square IDs and values are piece IDs such as `wking`, `bpawn4`, or `None`.

Examples:

- `11` -> file `a`, rank `1`
- `58` -> file `e`, rank `8`
- `17` -> file `a`, rank `7`

This coordinate scheme is used throughout move generation and rendering.

### Rendering

- `design/board.py` draws the 64 squares
- `design/square.py` handles alternating square colors
- `design/build_pieces.py` maps board positions to on-screen coordinates and draws the pieces
- `design/pieces/*.py` contains the turtle drawing logic for each piece type

### Interaction

`interaction/click.py` manages:

- selecting a piece
- reselecting another friendly piece
- deselecting by clicking the same square
- moving a piece
- switching turns
- flipping the board after each move
- writing game status messages

### Move Validation

`interaction/move_validation/check_valid.py` is the main rules module. It currently includes:

- pseudo-legal move generation
- legal move filtering
- same-color collision checks
- king safety checks
- attack detection
- check/checkmate/stalemate evaluation

Sliding pieces such as rooks, bishops, and queens use directional scanning rather than hardcoded destination lists.

## Running the Game

### Requirements

- Python 3 installed on your machine

### Start

From the project root:

```powershell
python main.py
```

If your system uses `py` instead of `python`, run:

```powershell
py main.py
```

## How To Play

1. Launch the game window.
2. Click one of the current player's pieces.
3. Legal destination squares will be highlighted.
4. Click a highlighted destination square to move.
5. After a valid move, the turn switches and the board flips for the next player.

Status text at the top of the window shows:

- whose turn it is
- which piece is selected
- whether a move is invalid
- check
- checkmate
- stalemate

## Current Rule Support

Implemented now:

- normal piece movement
- pawn single-step movement
- pawn two-step movement from the starting rank
- pawn diagonal captures
- prevention of illegal self-check moves
- check detection
- checkmate detection
- stalemate detection

## Current Limitations

The game is playable, but it is not yet a complete tournament-rules chess implementation. Based on the current code, these features are not implemented or are not yet fully handled:

- castling
- en passant
- pawn promotion
- move history
- undo/redo
- clock or timers
- PGN/FEN import/export
- AI opponent
- explicit restart button or menu
- automated test coverage beyond a small scratch file

## Customization

### Change The Color Theme

Board and piece colors are defined in `initial_constants.py` inside the `palette` dictionary.

To switch themes, change:

```python
palette_name = "A"
```

to another available palette such as `"B"`, `"C"`, `"D"`, or `"E"`.

## Notable Files

- [`main.py`](/c:/Users/Yusuftoo/chess%20board/main.py): application startup
- [`initial_constants.py`](/c:/Users/Yusuftoo/chess%20board/initial_constants.py): initial board state, palette data, coordinate maps
- [`interaction/click.py`](/c:/Users/Yusuftoo/chess%20board/interaction/click.py): user interaction and turn flow
- [`interaction/move_validation/check_valid.py`](/c:/Users/Yusuftoo/chess%20board/interaction/move_validation/check_valid.py): rules and game-state logic
- [`design/build_pieces.py`](/c:/Users/Yusuftoo/chess%20board/design/build_pieces.py): piece placement and highlighting

## Ideas For Future Improvements

- add castling, promotion, and en passant
- add a reset/new game option
- add move logging in algebraic notation
- add captured-piece display
- improve status UI and board labels
- create proper automated tests for move generation and game states
- add a computer opponent
- package the game into a cleaner application structure

## Summary

This project is a solid turtle-based chess game with a real playable loop, graphical rendering, legal move filtering, and endgame-state detection. It is a good foundation for extending into a fuller chess implementation with advanced rules, tests, and UI polish.
