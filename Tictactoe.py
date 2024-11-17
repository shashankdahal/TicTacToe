import pandas as pd
space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])
print(space_matrix)
i=0
game_won = False
while i < 9:
    j=1
    if j== 1:
        row = int(input(f"Player 'X', enter the row (1, 2, or 3): ")) - 1
        col = int(input(f"Player 'X', enter the column (1, 2, or 3): ")) - 1  
        if space_matrix.iloc[row, col] == ' ':
            space_matrix.iloc[row, col] = 'X'
            print(f"\nUpdated matrix after placing 'X':")
            print(space_matrix)
            i=i+1
            j = 0
            
            for k in range(3):
                if space_matrix.iloc[k, 0] == space_matrix.iloc[k, 1] == space_matrix.iloc[k, 2] == "X" :
                    print("Player X wins")
                    game_won= True
                    break
            for k in range(3):
                if space_matrix.iloc[0, k] == space_matrix.iloc[1, k] == space_matrix.iloc[2, k] == "X" :
                    print("Player X wins")
                    game_won= True
                    break
            if space_matrix.iloc[0, 0] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 2] == "X":
                    print("Player X wins")
                    game_won= True
                    break            
            if space_matrix.iloc[0, 2] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 0] == "X":
                    print("Player X wins")
                    game_won= True
                    break        
        elif space_matrix.iloc[row, col]== 'X' or space_matrix.iloc[row, col] =='O' :
            print("Invalid Entry, the space is already occupied")
            j = 1
        if game_won == True :
            break

    if j== 0:
        row = int(input(f"Player 'O', enter the row (1, 2, or 3): ")) - 1
        col = int(input(f"Player 'O', enter the column (1, 2, or 3): ")) - 1  
        if space_matrix.iloc[row, col] == ' ':
            space_matrix.iloc[row, col] = 'O'
            print(f"\nUpdated matrix after placing 'O':")
            print(space_matrix)
            i=i+1
            j= 1
            for k in range(3):
                if space_matrix.iloc[k, 0] == space_matrix.iloc[k, 1] == space_matrix.iloc[k, 2] == "O" :
                    print("Player O wins")
                    game_won= True
                    break
            for k in range(3):
                if space_matrix.iloc[0, k] == space_matrix.iloc[1, k] == space_matrix.iloc[2, k] == "O" :
                    print("Player O wins")
                    game_won= True
                    break
            if space_matrix.iloc[0, 0] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 2] == "O":
                    print("Player O wins")
                    game_won= True
                    break            
            if space_matrix.iloc[0, 2] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 0] == "O":
                    print("Player O wins")
                    game_won= True
                    break       
        elif space_matrix.iloc[row, col]== 'X' or space_matrix.iloc[row, col] =='O' :
            print("Invalid Entry, the space is already occupied")
            j = 0
        if game_won == True :
            break
print("Game Over")
space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])