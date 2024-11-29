import pandas as pd
import numpy as np
import os

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(board.to_string(header=False))

def check_winner(board, symbol):
    """Check if a player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board.iloc[i, :] == symbol) or all(board.iloc[:, i] == symbol):
            return True
    # Check diagonals
    if board.iloc[0, 0] == board.iloc[1, 1] == board.iloc[2, 2] == symbol:
        return True
    if board.iloc[0, 2] == board.iloc[1, 1] == board.iloc[2, 0] == symbol:
        return True
    return False

def get_player_input(player_name, board):
    """Get valid row and column input from player."""
    while True:
        try:
            row = int(input(f"{player_name}, enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"{player_name}, enter the column (1, 2, or 3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 1 and 3.")
            elif board.iloc[row, col] != '|':
                print("Invalid move! That spot is already taken.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Please enter numeric values for row and column.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    *************************************
    *                                   *
    *     WELCOME TO MY TICTACTOE       *
    *                                   *
    *************************************
    """)

    print("""
    *************************************
    Press 1 To Play Game
    Press 2 To see Rules
    Press 3 To Exit
    *************************************
    """)
    
    option = int(input("1 or 2 or 3 \n"))

    if option == 2:
        print("""
    *************************************
           RULES :
      - 2 Player mode game. Player 1 to be alloted X and second player O

      - Enter the player names

      - The game is over when 3 pairs of same symbols are aligned, someone wins and if all 9 boxes are filled the game is draw and over.
      
      - The game is based using a 3x3 Matrix where the input fields are the rows and columns. The user is prompted to enter the row number
        and the column number for their symbol. 

      - Valid entries are only X and O. The game crashes for any invalid input of numbers exceeding 3.
    *************************************    

           """)
        input("#####TO PLAY GAME PRESS P#####\n")

    if option == 1 or input("Press 'P' to play: ").lower() == 'p':
        # Initialize board
        board = pd.DataFrame(np.full((3, 3), '|'))
        print_board(board)

        # Player names
        p1 = input("Player 1 name for symbol X: ")
        p2 = input("Player 2 name for symbol O: ")

        turns = 0
        game_won = False

        while turns < 9 and not game_won:
            current_player = p1 if turns % 2 == 0 else p2
            symbol = '|X' if turns % 2 == 0 else '|O'

            # Get player input
            row, col = get_player_input(current_player, board)

            # Make the move
            board.iloc[row, col] = symbol
            print_board(board)

            # Check for winner
            if check_winner(board, symbol):
                print(f"\n Player {current_player} wins!")
                game_won = True

            turns += 1

        if not game_won:
            print("\n It's a draw!")

        print("#######Game Over!########")

    if option == 3:
        exit()

if __name__ == "__main__":
    main()
