# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from random import randint, choice
import math 
from copy import deepcopy
import sys



def draw(board):
  
   # prints board line by line  
    print(board[0])
    print("--------------")
    print(board[1])
    print("--------------")
    print(board[2])
    

    
    
def available(location, board):
    
    
    for i in range(len(board)):
        
        check = str("".join(board[i]))
        
        #not sure why i had to redeclare them as strings but i had to
        if str(location) not in str(check):
            continue
        elif str(location) in str(check):
            return True
    return False
  
                                 
"""
    if int(location) not in board:
        return True
    else: 
        return False
"""

def mark(player, location, board):

    
    #cycles through each possition to find where to place the mark
    mark = int(location)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X' or board[i][j] == 'O' or mark != int(board[i][j]):
                continue
            else:  
                if player == 'X':
                    board[i][j] = 'X'
                    return board
                    break
                elif player == 'O':
                    board[i][j] = 'O'
                    return board
                    break
        
def board_copy(board):
    
    #returns a copy of the board and it is copied into a new reference
    dubboard = []
    
    dubboard = deepcopy(board)
    return dubboard

def computer_turn(cletter,pletter,board):
    """
    #random space selection for testing
    i = randint(1,9)
    return i
    """
    
    
    #makes a winning move
    for i in range(1,10):
        dubboard = board_copy(board)
        if available(i,dubboard):
            mark(cletter,i,dubboard)
            if check_win(dubboard) == True:
                return i
                         
    
    #blocks a winning move
    for i in range(1,9):
        dubboard = board_copy(board)
        if available(i,dubboard):
            mark(pletter,i,dubboard)
            if check_win(dubboard)==True:
                return i 
                    
    
    #takes corner
    for x in range(1,5):
        i = choice([1,3,7,9])
        if available(i,dubboard):
            return i
            break
    
    #takes center
    if available(5,dubboard):
        return 5
        
    
    #takes edges
    for x in range (1,5):
        i = choice([2,4,6,8])
        if available(i,dubboard):    
            return i
            break
   
    

def check_win(board):
    #returns true if won and false if not
    
    checkX = ['X','X','X']
    checkO = ['O','O','O']
     # diagonal win
    if board[0][0] == 'X' and board[1][1] =='X' and board[2][2] == 'X' or board[0][0] == 'O' and board[1][1] =='O' and board[2][2] == 'O':
        return True
            #anti diagonal win
    elif board[0][2] == 'X' and board[1][1] =='X' and board[2][0] == 'X' or board[0][2] == 'O' and board[1][1] =='O' and board[2][0] == 'O':
        return True
    else:
        for i in range(len(board)):
            if board[i] == checkX or board[i] == checkO:#checks horizolate win
                return True
            #checks vertical grossly
            elif board[0][i] == 'X' and board[1][i] =='X' and board[2][i]=='X' or board[0][i] == 'O' and board[1][i] =='O' and board[2][i]=='O':
                return True
           
    return False
def check_tie(turns):
    #counts turns to determine tie returns true if tied or false if not
    
    if turns<9:
        return False
    else:
        return True
    
    
def choose_letter():
    #lets player determine the letter
    
    letter= ''
    while not(letter == 'O' or letter =='X'):
        
        letter = raw_input('do you want to X or O: ').upper()
        
    if letter == 'X':
        return['X','O']
    elif letter =='O':
        return['O','X']
    
def choose_first():
    ri = randint(0,1)
    if ri == 0:
        return "computer"
    else:
        return "player"
    
def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 *'-' + "o")
    
def display(message):
  
    print("|{:^35s}|".format(message))
    
def main():
    pletter,cletter = choose_letter()
    turn = choose_first()
    if turn == "player":
        current_player = pletter
    else:
        current_player = cletter
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
   # player = ['X', 'O']
    #turn = randint(0, 1)
    turns = 0
    win = False
    tie = False
    while(not win and not tie):
        # switch players
        """
        turn = (turn + 1) % 2
        current_player = player[turn] # contains 'X' or 'O'
        """
        
        turns+=1 
        
        
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        if current_player == pletter:
            while True:
                location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
                if available(location, board):
                    break # Only the user input loop, main loop does NOT break
                else:
                    print("Selection not available!")
        #gives computer a section to mark but its random
        elif current_player == cletter:
            while True:
                location = computer_turn(cletter, pletter, board)
                if available(location, board):
                    break
                
                    
                                
        dashes()
        
        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)
        
       
        
        # check for win
        win = check_win(board)
        if win == True:
            break
        # check for tie
        tie = check_tie(turns)
        #switches player and computer
        if current_player == pletter:
            current_player = cletter
        elif current_player == cletter:
            current_player = pletter

    # Display game over message after a win or a tie
    
    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if(tie):
        display("Tie!")
        dashes()
        answer = raw_input("do you want to play again?[y,n]:").lower()
        if answer == 'y':
            main()
        else:
            sys.exit()
    elif(win):
        if current_player == pletter:
            display("YOU WIN!")
            display(pletter)
            dashes()
            answer = raw_input("do you want to play again?[y,n]:").lower()
            if answer == 'y':
                main()
            else:
                sys.exit()
            
        elif current_player == cletter:
            display("YOU LOST!")
            dashes()
            answer = raw_input("do you want to play again?[y,n]:").lower()
            if answer == 'y':
                main()
            else:
                sys.exit()
    dashes()
  
# Run the game
main()
