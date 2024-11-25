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
    #creating a 3x3 empty matrix as an interface for playing Tictactoe
    space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])
    print(space_matrix)
    #variable declaration
    i=0 #identifier if game is over or not, i.e all spaces filled or not
    game_won = False #bollean field to break if game is won or not
    #input players
    p1= input("Player first name for symbol X \n")
    p2= input("Player second name for symbol O \n")
    #9 is the total inputs
    while i < 9:
        j=1 #check variable. 1 is for player 1 and 0 is for player 2
        if j== 1: #condition for player 1 to put X
            print("********player",p1,"***********")
            row = int(input(f"enter the row (1, 2, or 3): ")) - 1 #row variable of matrix
            col = int(input(f"enter the column (1, 2, or 3): ")) - 1 #column variable of matrix
            if space_matrix.iloc[row, col] == ' ': #using only unoccupied spaces
                space_matrix.iloc[row, col] = 'X' #assign the row and col
                print(f"\nUpdated matrix after placing 'X':")
                print(space_matrix)
                i=i+1 #adding i value when space is filled
                j = 0 #this signifies the next step is for player 2 to put O
                #condition check if the game is won or not
                for k in range(3): #if all X in any 3 consequtive rows
                    if space_matrix.iloc[k, 0] == space_matrix.iloc[k, 1] == space_matrix.iloc[k, 2] == "X" :
                        print("Player",p1, "wins")
                        game_won= True
                        break
                for k in range(3): #if all X in any 3 consequtive rows
                    if space_matrix.iloc[0, k] == space_matrix.iloc[1, k] == space_matrix.iloc[2, k] == "X" :
                        print("Player",p1, "wins")
                        game_won= True
                        break
                if space_matrix.iloc[0, 0] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 2] == "X": #if all X in first diagonal
                        print("Player",p1, "wins")
                        game_won= True
                        break            
                if space_matrix.iloc[0, 2] == space_matrix.iloc[1, 1] == space_matrix.iloc[2, 0] == "X": #if all X in another diagonal
                        print("Player",p1, "wins")
                        game_won= True
                        break        
            elif space_matrix.iloc[row, col]== 'X' or space_matrix.iloc[row, col] =='O' : #if user puts entry in a space where there is already a value
                print("Invalid Entry, the space is already occupied")
                j = 1
            if game_won == True : #any point if the game is won
                break
        if i>= 9: #when all space is occupied and there is no winner
            print("Draw")
            break
        if j== 0: #same above process repeated for player 2
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
    #At the end 
    print("Game Over")
    #Reseting the board after game over
    space_matrix = pd.DataFrame([[' ' for _ in range(3)] for _ in range(3)])

if option == 2:
     exit()
     