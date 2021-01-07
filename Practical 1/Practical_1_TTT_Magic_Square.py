# Practical 1 Tic-Tac-Toe Using Magic Square Method
# Importing the library
import random

# Some Data Structure Required during Execution
## Board Data structure for displaying the game
board=['-','-','-',
        '-','-','-',
        '-','-','-']
## Magic Square Data structure for playing in the game play Data structure
magic_square=[2,7,6,
            9,5,1,
            4,3,8]
## Game Play data structure for placing the moves on Board
gameplay=[0,0,0,
        0,0,0,
        0,0,0]

## Computer Move Index represented as arr[i]=i-1
computer_index=[1,2,3,4,5,6,7,8,9]

## To Store Computer Moves with respect to Magic Square
computer_moves=[]
## To Store Human moves with respect to Magic Square
human_moves=[]

# Utility Function Required by the program
# Function To Display any 1d array of length 9 in 3X3 form
def display_board(arr):
    print(str(arr[0]) + ' | ' + str(arr[1]) + ' | ' + str(arr[2]))
    print("---------")
    print(str(arr[3]) + ' | ' + str(arr[4]) + ' | ' + str(arr[5]))
    print("---------")
    print(str(arr[6]) + ' | ' + str(arr[7]) + ' | ' + str(arr[8]))

# Function to perform computer move
def computer_move_operation(move):
    """
    Exchange the exact values from magic square to 
    gameplay and board(choice) at specified index-1
    append the corresponding magic_square value in computer move array
    display
    """
    print("Current Computer Move",move)
    gameplay[move-1]=magic_square[move-1]
    board[move-1]=computer_choice

    computer_moves.append(magic_square[move-1])

    display_board(board)

# Function to perform Human move
def human_move_operation(move):
    """
    Exchange the exact values from magic square to 
    gameplay and board(choice) at specified index-1
    append the corresponding magic_square value in Human move array
    display
    """
    gameplay[move-1]=magic_square[move-1]
    board[move-1]=human_choice.upper()
    
    human_moves.append(magic_square[move-1])
    display_board(board)

# Function To check win Possiblity
def check_win(arr):
    """
    A Function for checking the winning possiblites using Magic Sqaure Concept
    It check for both the players if computer is playing then it checks for it 
    like return 1-D Array with true and value which is to be marked with corresponding 
    index and check the human wining for blocking the move.
    It also check for human wining it true return a 1-D array of True else return false.
    The function is divided into 3 part checking that are for Row, Column and Diagonal. 
    """

    # Row
    for col in range(0,7,3):
        current_row=[gameplay[col],gameplay[col+1],gameplay[col+2]]

        com_elements=list(set(current_row) & set(arr))
        if len(com_elements) >=2:                               # For Wining the row should have atleast 2 elements from Move array
            x=15-sum(com_elements)
            # Special Checking for checking the win of own where difference should be zero and all the elements should be available in Move array
            if x == 0 and (current_row[0] in arr) and (current_row[1] in arr) and (current_row[2] in arr):
                return [True]
            # Return the Difference and check that value is not taken in the board
            if x <= 9 and gameplay[magic_square.index(x)]==0:
                return [True,x]
            
    # Column
    for row in range(3):
        current_col=[gameplay[row],gameplay[row+3],gameplay[row+6]]

        com_elements=list(set(current_col) & set(arr))
        if len(com_elements) >=2:                               # For Wining the column should have atleast 2 elements from Move array
            y=15-sum(com_elements)
            # Special Checking for checking the win of own where difference should be zero and all the elements should be available in Move array
            if y == 0 and (current_col[0] in arr) and (current_col[1] in arr) and (current_col[2] in arr):
                return [True]
            # Return the Difference and check that value is not taken in the board
            if y <= 9 and gameplay[magic_square.index(y)]==0:
                return [True,y]

    # Diagonal
    for diag in [0,2]:
        if diag == 0:
            current_diag=[gameplay[diag],gameplay[diag+4],gameplay[diag+8]]
        if diag == 2:
            current_diag=[gameplay[diag],gameplay[diag+2],gameplay[diag+4]]

        com_elements=list(set(current_diag) & set(arr))
        if len(com_elements) >= 2:                              # For Wining the diagonal should have atleast 2 elements from Move array
            z=15-sum(com_elements)
            # Special Checking for checking the win of own where difference should be zero and all the elements should be available in Move array
            if z == 0 and (current_diag[0] in arr) and (current_diag[1] in arr) and (current_diag[2] in arr):
                return [True]
            # Return the Difference and check that value is not taken in the board
            if z <= 9 and gameplay[magic_square.index(z)]==0:
                return [True,z]
    
    return [False]

def play_game(current_turn):
    """
    The Main Function Of the Program which Controls all the logic behind Wining, Blocking, Placing Moves For Computer.
    This Function Also Enlist Different Scenarios for both Computer and Human, like who to process with first turn and afterwords for each of it.

    The First Two condition Places the basic First Moves for both.
    The third conditon which is else part controls further steps in game and set the game in systematic manner.    
    """
    if start_turn==1 and current_turn==0:
        current_computer_move=random.choice(computer_index)
        computer_move_operation(current_computer_move)

    elif start_turn==2 and current_turn==0:
        current_human_move=int(input(" Enter place the of Move from 1 to 9 : "))
        if current_human_move >=1 and current_human_move <= 9 and gameplay[current_human_move-1]==0:
            human_move_operation(current_human_move)
        else:
            print(" Enter Valid Input")
            play_game(current_turn)
    
    else:
        # When First Player is Computer
        if start_turn == 1:
            """
            When First Turn is Played by Computer/System
            First Condition Places the move randomly because its the second move for Computer.
            In Second Condion the Computer is trying to check some more scenerio's at particular turns of system
                - If it is itself wining then find the move with corresponding index and check for wining and exit the porgram.
                - If human is wing then block the move of his/her and check for wining and exit the porgram.
                - If nothing is Happening then place it randomly while checking the gameboard or gameplay and check for wining and exit the porgram.
            In Last else part where the turn is of human, it is asking the move and checking fot the wining, if it true then exit the game.
            """
            if current_turn == 2:
                current_computer_move=random.choice(computer_index)
                if gameplay[current_computer_move-1]==0 and (magic_square[current_computer_move-1] not in human_moves):
                    computer_move_operation(current_computer_move)
                else:
                    play_game(current_turn)
            
            elif current_turn in [4,6,8]:
                check_human_win=check_win(human_moves)
                check_computer_win=check_win(computer_moves)

                if check_computer_win[0] and gameplay[magic_square.index(check_computer_win[1])] == 0:
                    current_computer_move=magic_square.index(check_computer_win[1])
                    computer_move_operation(current_computer_move+1)
                    #print("Board from Computer win")
                    check_computer_win=check_win(computer_moves)
                    if check_computer_win[0] and len(check_computer_win) == 1:
                        print("Computer Has Won! Winnner")
                        exit()
                
                elif check_human_win[0] and gameplay[magic_square.index(check_human_win[1])] == 0:
                    current_computer_move=magic_square.index(check_human_win[1])
                    computer_move_operation(current_computer_move+1)
                    #print("Board From human wining")
                    check_computer_win=check_win(computer_moves)
                    if check_computer_win[0] and len(check_computer_win) == 1:
                        print("Computer Has Won! Winnner")
                        exit()
                
                else:
                    current_computer_move=random.choice(computer_index)
                    if gameplay[current_computer_move-1]==0 and (magic_square[current_computer_move-1] not in human_moves):
                        computer_move_operation(current_computer_move)
                        #print("Board from actual random turn")
                        check_computer_win=check_win(computer_moves)
                        if check_computer_win[0] and len(check_computer_win) == 1:
                            print("Computer Has Won! Winnner")
                            exit()
                    else:
                        play_game(current_turn)
                    
                    
            else:
                current_human_move=int(input("Enter place the of Move from 1 to 9 : "))
                if current_human_move >=1 and current_human_move <= 9 and gameplay[current_human_move-1] == 0:
                    check_human_win=check_win(human_moves)
                    human_move_operation(current_human_move)
                    if check_human_win[0] and (magic_square.index(check_human_win[1])+1) == current_human_move:
                        print("You Have Won the game")
                        exit()
                else:
                    print(" Enter Valid Input. Move already taken.")
                    play_game(current_turn)
        
        # When First Player is Human
        if start_turn == 2: 
            """
            When First Turn is Played by Human/User, It places the Move according to input and checks for wining chances of him.
            First Condition Places the move according to the user because its the second move for him.
            In Second Condion the Computer is trying to check some more scenerio's at particular turns of system
                - First condition places the move randomly because its the second move for Computer.
                - In Second Subcondtions its checking different Scenerio's such as
                    - If it is itself wining then find the move with corresponding index and check for wining and exit the porgram.
                    - If human is wing then block the move of his/her and check for wining and exit the porgram.
                    - If nothing is Happening then place it randomly while checking the gameboard or gameplay and check for wining and exit the program.
            """
            if current_turn in [2,4,6,8]:
                current_human_move=int(input("Enter place the of Move from 1 to 9 : "))
                if current_human_move >=1 and current_human_move <= 9 and gameplay[current_human_move-1]==0:
                    check_human_win=check_win(human_moves)
                    human_move_operation(current_human_move)
                    #print(check_human_win)
                    if check_human_win[0] and (magic_square.index(check_human_win[1])+1) == current_human_move:
                        print("You have won the game")
                        exit()
                else:
                    print(" Enter Valid Input or Move already taken.")
                    play_game(current_turn)
            else:
                if current_turn == 1:
                    current_computer_move=random.choice(computer_index)
                    if gameplay[current_computer_move-1]==0:
                        computer_move_operation(current_computer_move)
                    else:
                        play_game(current_turn)
            
                elif current_turn in [3,5,7]:
                    check_human_win=check_win(human_moves)
                    check_computer_win=check_win(computer_moves)
                    
                    if check_computer_win[0] and gameplay[magic_square.index(check_computer_win[1])]  == 0:
                        current_computer_move=magic_square.index(check_computer_win[1])
                        computer_move_operation(current_computer_move+1)
                        #print("Board from Computer win")
                        check_computer_win=check_win(computer_moves)
                        if check_computer_win[0] and len(check_computer_win) == 1:
                            print("Computer Has Won! Winnner")
                            exit()
                        
                    elif check_human_win[0] and gameplay[magic_square.index(check_human_win[1])] == 0:
                        current_computer_move=magic_square.index(check_human_win[1])
                        computer_move_operation(current_computer_move+1)
                        #print("Board From human wining")
                        check_computer_win=check_win(computer_moves)
                        if check_computer_win[0] and len(check_computer_win) == 1:
                            print("Computer Has Won! Winnner")
                            exit()

                    else:
                        current_computer_move=random.choice(computer_index)
                        if gameplay[current_computer_move-1]==0 and (magic_square[current_computer_move-1] not in human_moves):
                            computer_move_operation(current_computer_move)
                            #print("Board from actual random turn")
                            check_computer_win=check_win(computer_moves)
                            if check_computer_win[0] and len(check_computer_win) == 1:
                                print("Computer Has Won! Winnner")
                                exit()
                        else:
                            play_game(current_turn)

# Introduction Part Containiing the Board and Magic Square Part
print()
print("Intial Board and corresponding Magic Square")
print()
display_board(board)
print()
print("#####################################################################")
print("Magic Square Concept Sum will be 15 for each row, column and diagonal")
print("#####################################################################")
print()
display_board(magic_square)
print()

# Main Program
human_choice=str(input(" Enter Your preference of symbol from 'X' or 'O': "))       # Variable for storing the Choice of Human
if human_choice=='X' or human_choice=='x':
    computer_choice='O'
else:
    computer_choice='X'
print(" So Computer will play using : ",computer_choice)                            # Variable for Storing the Choice of Computer

# Varibale which starts the game with any player at random
start_turn=random.randint(1,2)

# For Loop for looping the turns between Human and Computer
# also the loop reaches for a DRAW if no one wins
for i in range(10):
    if i==9:                                                                        # Condition if loop reaches to end then should DRAW the game
        print("No Winner This is Draw")
        break
    else:
        print("TURN : ",i+1)                                                        # Variable for Showing the Turn iteration between play
        if start_turn==1 and i==0:
            print("First Move is played by Computer")
            play_game(i)
        elif start_turn==2 and i==0:
            print("Play your First Move")
            play_game(i)
        else:
            play_game(i)