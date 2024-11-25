import pandas as pd
import numpy
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("""
*************************************
*                                   *
*     WELCOME TO MY TICTACTOE       *
*                                   *
*************************************
      
      RULES :
      - 2 Player mode game. Player 1 to be alloted X and second player Y
      - Enter the player names
      - The game is over when 3 pairs of same symbols are aligned, someone wins and if all 9 boxes are filled the game is draw and over.
""")
print("""
            *************************************
            Press 1 To Play Game
            Press 2 To Exit
            *************************************
            """)
option = int(input("1 or 2 \n"))
if option == 1:
    space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])
    print(space_matrix)
    i=0
    game_won = False
    p1= input("Player first name for symbol X \n")
    p2= input("Player second name for symbol O \n")
    while i < 9:
        j=1
        if j== 1:
            print("********player",p1,"***********")
            row = int(input(f"enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"enter the column (1, 2, or 3): ")) - 1 
            if space_matrix.iloc[row, col] == ' ':
                space_matrix.iloc[row, col] = 'X'
                print(f"\nUpdated matrix after placing 'X':")
                print(space_matrix)
                i=i+1
                j = 0
                
                for k in range(3):
                    if space_matrix.iloc[k, 0] == space_matrix.iloc[k, 1] == space_matrix.iloc[k, 2] == "X" :
                        print("Player",p1, "wins")
                        game_won= True
                        break
                for k in range(3):
                    if space_matrix.iloc[0, k] == space_matrix.iloc[1, k] == space_matrix.iloc[2, k] == "X" :
                        print("Player",p1, "wins")
                        game_won= True
                        break
                if space_matrix.iloc[0, 0] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 2] == "X":
                        print("Player",p1, "wins")
                        game_won= True
                        break            
                if space_matrix.iloc[0, 2] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 0] == "X":
                        print("Player",p1, "wins")
                        game_won= True
                        break        
            elif space_matrix.iloc[row, col]== 'X' or space_matrix.iloc[row, col] =='O' :
                print("Invalid Entry, the space is already occupied")
                j = 1
            if game_won == True :
                break
        if i>= 9:
            print("Draw")
            break
        if j== 0:
            print("********player",p2,"***********")
            row = int(input(f"enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"enter the column (1, 2, or 3): ")) - 1  
            if space_matrix.iloc[row, col] == ' ':
                space_matrix.iloc[row, col] = 'O'
                print(f"\nUpdated matrix after placing 'O':")
                print(space_matrix)
                i=i+1
                j= 1
                for k in range(3):
                    if space_matrix.iloc[k, 0] == space_matrix.iloc[k, 1] == space_matrix.iloc[k, 2] == "O" :
                        print("Player",p2, "wins")
                        game_won= True
                        break
                for k in range(3):
                    if space_matrix.iloc[0, k] == space_matrix.iloc[1, k] == space_matrix.iloc[2, k] == "O" :
                        print("Player",p2, "wins")
                        game_won= True
                        break
                if space_matrix.iloc[0, 0] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 2] == "O":
                        print("Player",p2, "wins")
                        game_won= True
                        break            
                if space_matrix.iloc[0, 2] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 0] == "O":
                        print("Player",p2, "wins")
                        game_won= True
                        break       
            elif space_matrix.iloc[row, col]== 'X' or space_matrix.iloc[row, col] =='O' :
                print("Invalid Entry, the space is already occupied")
                j = 0
            if game_won == True :
                break
    print("Game Over")
    space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])

if option == 2:
     exit()