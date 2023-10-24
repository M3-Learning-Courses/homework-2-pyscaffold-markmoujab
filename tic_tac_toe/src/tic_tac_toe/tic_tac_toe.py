import random
import pyfiglet


def print_board(board):
    """
    Prints the Tic-Tac-Toe board to the console.

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))  # Print a row with cell values separated by " | "
        print("-" * 9)  # Print a horizontal line to separate rows

def check_win(board, player):
    """
    Checks if a player has won the game.

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
        player (str): The current player ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns for a win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals for a win
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    """
    Checks if the Tic-Tac-Toe board is full (no empty cells).

    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all([cell != ' ' for row in board for cell in row])

def main():
    """
    Main function to play the Tic-Tac-Toe game.

    The function initializes the game, handles player turns, and determines the winner.

    Args:
        None

    Returns:
        None
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Create an empty 3x3 board
    player = 'X'  # Initialize the first player
    win = False  # Flag to track if a player has won

    print("Welcome to Tic-Tac-Toe!")

    # Main game loop
    while not win and not is_board_full(board):
        print_board(board)  # Display the current state of the board
        print(f"Player {player}'s turn")
        
        # Get the player's move (row and column)
        row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
        
        # Check for invalid moves
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue
        
        # Update the board with the player's move
        board[row - 1][col - 1] = player
        
        # Check if the current player has won
        if check_win(board, player):
            win = True
            print_board(board)  # Display the final state of the board
            print(f"Player {player} wins!")
        else:
            player = 'O' if player == 'X' else 'X'  # Switch players for the next turn
    
    # Game over: check for a tie (no winner)
    if not win:
        print_board(board)  # Display the final state of the board
        print("It's a tie!")

# Entry point to the program
if __name__ == "__main__":
    main()  # Call the main function to start the game
