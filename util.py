import random
from rich.console import Console

console = Console()
conv = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

def display_board(board) -> None:
    '''
    The function displays the current status of the board in a user-friendly format.
    :param board: A 2D list representing the Tic Tac Toe board.
    :return: None
    '''

    console.print(f'''
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    ''')

def enter_move(board) -> list:
    '''
    The function asks the user for their move, checks if the input is valid, and updates the board accordingly.
    :param board: A 2D list representing the Tic Tac Toe board.
    :return: The updated board after the user's move.
    '''
    # user_move = int(input("Please enter your move: "))

    invalid_move = True
    while invalid_move:
        try:
            user_move = int(input("Please enter your move: "))
            if isinstance(board[conv.get(user_move)[0]][conv.get(user_move)[1]], int):
                board[conv.get(user_move)[0]][conv.get(user_move)[1]] = 'O'
                display_board(board)
                invalid_move = False
            else:
                user_move = int(input("Please enter a valid move: "))
        except ValueError:
            console.print("Invalid input. Please enter a number between 1 and 9.", style="red")
            continue
    return board

def make_list_of_free_fields(board) -> list:
    '''
    The function creates a list of all the free squares on the board.
    :param board: A 2D list representing the Tic Tac Toe board.
    :return: A list of tuples representing the free squares, where each tuple contains the row and column indices.
    '''

    free_fields = []
    for i in board:
        for x in i:
            if isinstance(x, int):
                free_fields.append((i, x))
    return free_fields

def victory_for(board, sign) -> bool:
    '''
    The function checks if there is a victory for the given sign ('O' for user, 'X' for computer).
    :param board: A 2D list representing the Tic Tac Toe board.
    :param sign: A string representing the sign to check for victory ('O' or 'X').
    :return: True if there is a victory or a tie, False otherwise.
    '''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if sign == 'O':
                console.print("You won!", style="bold green")
            else:
                console.print("Computer won!", style="bold red")
            return True
        if board[0][i] == board[1][i] == board[2][i]:
            if sign == 'O':
                console.print("You won!", style="bold green")
            else:
                console.print("Computer won!", style="bold red")
            return True
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if sign == 'O':
            console.print("You won!", style="bold green")
        else:
            console.print("Computer won!", style="bold red")
        return True
    if len(make_list_of_free_fields(board)) == 0:
        console.print("Tie", style="bold yellow")
        return True
    return False

def draw_move(board) -> list:
    '''
    The function draws the computer's move on the board.
    :param board: A 2D list representing the Tic Tac Toe board.
    :return: The updated board after the computer's move.
    '''
    # free_fields = make_list_of_free_fields(board)
    # if free_fields:
    #     row, col = random.choice(free_fields)
    #     board[row][col] = 'X'
    #     display_board(board)

    free_fields = []
    for x in board:
        for y in x:
            if isinstance(y, int):
                free_fields.append(y)
    comp_move = random.choice(free_fields)
    board[conv.get(comp_move)[0]][conv.get(comp_move)[1]] = 'X'
    display_board(board)
    
    return board