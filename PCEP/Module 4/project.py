import random

def display_board(board):
    """Display the current status of the board.

    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.
    """
    size = len(board)
    # Find the maximum width needed for any cell
    max_cell_width = max(len(str(cell)) for row in board for cell in row)
    # Make the cell more square by increasing the width
    cell_width = max(5, max_cell_width + 2)
    horiz = "+" + ("-" * (cell_width + 2) + "+") * size

    lines = []
    for row in board:
        lines.append(horiz)
        lines.append("|" + (" " * (cell_width + 2) + "|") * size)
        value_line = ""
        for cell in row:
            value_line += f"| {str(cell).center(cell_width)} "
        value_line += "|"
        lines.append(value_line)
        lines.append("|" + (" " * (cell_width + 2) + "|") * size)
    lines.append(horiz)
    print('\n'.join(lines))

def enter_move(board):
    """Asks the user for their move and updates the board accordingly

    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.
    
    Returns:
        list of lists: updated board with the users move.
    """
    free_squares = make_list_of_free_fields(board)
    size = len(board)
    while True:
        try:
            user_move = int(input(f"Please select which square you would like to put a O on (1-{size**2}): "))
            if user_move < 1 or user_move > size**2:
                print(f"The square on the grid must be a positive integer between 1 and {size**2}, please try again")
                continue
            
            row, col = divmod(user_move-1, size)
            
            if (row,col) not in free_squares:
                print("This square on the grid is already taken, please try again")
            else:
                board[row][col] = "O"
                return board
        except ValueError:
            print("The square on the grid must be an integer, please try again.")


def make_list_of_free_fields(board):
    """Return a list of free squares on the board.

    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.
        
    Returns: 
        list of tuples: coordinates of free spaces on the board.
    """
    free_squares = []
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if value not in ["X", "O"]:
                free_squares.append((row_idx, col_idx))
    return free_squares


def victory_for(board, sign):
    """Determines the boards status and announces a winner.

    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.
        sign (string): The sign of the player or computer i.e. a "O" or "X".
        
    Returns: 
        Boolean: The status of the game, i.e. whether the game is finished or not.
    """

    #check columns
    for col_idx in range(len(board[0])):
        if all(board[row_idx][col_idx] == sign for row_idx in range(len(board))):
            print("You Win!" if sign == "O" else "Computer Wins.")
            return False

    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            print("You Win!" if sign == "O" else "Computer Wins.")
            return False

    # Check main diagonal
    if all(board[i][i] == sign for i in range(len(board))):
        print("You Win!" if sign == "O" else "Computer Wins.")
        return False

    # Check anti-diagonal
    if all((board[i][len(board)-1-i] == sign for i in range(len(board)))):
        print("You Win!" if sign == "O" else "Computer Wins.")
        return False

    #check if the game is a draw
    free_squares = make_list_of_free_fields(board)
    if not free_squares:
        print("The game is a draw.")
        return False
    return True

def draw_move(board):
    """Updates the board with computer's move.
    
    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.

    Returns:
        list of list: The updated board after the computer's move.
    """
    free_squares = make_list_of_free_fields(board)
    size = len(board)
    if not free_squares:
        return board # No move possible
    center = (size // 2, size // 2)
    if center in free_squares:
        board[center[0]][center[1]] = "X"
    elif len(free_squares) == 1:
        board[free_squares[0][0]][free_squares[0][1]] = "X"
    else:
        rand = random.randint(0, len(free_squares) - 1)
        rand_square = free_squares[rand]
        board[rand_square[0]][rand_square[1]] = "X"
    return board
    
def main(board):
    """Runs the game of nougths and crosses.

    Args:
        board (list of list): list of list size (3 x 3) representing the board and its values.
    """
    print("Welcome to this game of noughts and crosses! You are noughts and the computer is crosses, the computer goes first")
    game_status = True
    while game_status:
        board = draw_move(board)
        display_board(board)
        game_status = victory_for(board,"X")
        if not game_status:
            break
        board = enter_move(board)
        display_board(board)
        game_status = victory_for(board,"O")


if __name__ == "__main__":
    size = 3
    board = [[size * i + j + 1 for j in range(size)] for i in range(size)]
    main(board)