# ------ logic ------

""" 
- Display Board
- Ask player to play and take input into variable (choose a number from 1 -9: ),
- Check if the input is valid: catch any invalid input
- If True:
    change the input location on the board,
    check if there is a winner, Tie or continue:
        if True:
            Winner is " "
        elif no Winner && board is full:
            Tie
        else:
            flipPlayer
  else:
      invalid input choose a number from 1 -9: ,
"""
import random
import sys

# ------ Global Variables ------


# board = [['-', '-', '-'],
#          ['-', '-', '-'],
#          ['-', '-', '-']]

board = {1: "-", 2: "-", 3: "-",
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}

currentPlayer = 'X'

logicPlayer = 'O'

dash = "-"

playerName = ''

playerMove = 0

winner = False

l = 0

# ------ functions ------


def displayBoard():

    global board
    print("\n")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + '   |    7 | 8 | 9 ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + '   |    4 | 5 | 6 ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + '   |    1 | 2 | 3 ')
    print("\n")


def playerTurn():
    global playerMove
    global board
    global currentPlayer
    global dash

    if currentPlayer == 'X':
        print(f'{playerName}\'s Turn you play X. ')
        print("\n")
        playerMove = input('Choose a Number from 1-9: ')

        while playerMove not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            playerMove = input('Choose a Number from 1-9: ')

        if board[int(playerMove)] == dash:
            board[int(playerMove)] = currentPlayer
            checkWinner(currentPlayer)
            return
        else:
            print("You can't go there. Go again.")
    else:
        computerLogic()


def computerLogic():
    global playerMove
    global currentPlayer
    global board
    global logicPlayer
    global dash
    emptyList = []
    boardValues = list(board.values())
    row1 = boardValues[:3]
    row2 = boardValues[3:6]
    row3 = boardValues[6:9]
    column1 = boardValues[:9:3]
    column2 = boardValues[1:9:3]
    column3 = boardValues[2:9:3]
    diagonal = boardValues[:9:4]
    diagonal2 = boardValues[2:7:2]
    corners = [1, 3, 7, 9]
    cornersPosition = random.choice(corners) # Random position from corners

    if board[5] == '-':
        board[5] = logicPlayer
        checkWinner(currentPlayer)
    elif '-' == board[1] == board[3] == board[7] == board[9]:
        board[cornersPosition] = logicPlayer
        checkWinner(currentPlayer)
    # To check if Computer have a chance to win
    elif row1.count('O') == 2 and dash in row1:
        board[row1.index(dash)+ 1] = logicPlayer
        checkWinner(currentPlayer)
    elif row2.count('O') == 2 and dash in row2:
        board[row2.index(dash)+ 4] = logicPlayer
        checkWinner(currentPlayer)
    elif row3.count('O') == 2 and dash in row3:
        board[row3.index(dash)+ 7] = logicPlayer
        checkWinner(currentPlayer)
    elif column1.count('O') == 2 and dash in column1:
        if column1.index(dash) == 0:
            board[column1.index(dash) + 1] = logicPlayer
            checkWinner(currentPlayer)
        elif column1.index(dash) == 1:
            board[column1.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif column1.index(dash) == 2:
            board[column1.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
    elif column2.count('O') == 2 and dash in column2:
        if column2.index(dash) == 0:
            board[column2.index(dash) + 2] = logicPlayer
            checkWinner(currentPlayer)
        elif column2.index(dash) == 1:
            board[column2.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif column2.index(dash) == 2:
            board[column2.index(dash) + 6] = logicPlayer
            checkWinner(currentPlayer)
    elif column3.count('O') == 2 and dash in column3:
        if column3.index(dash) == 0:
            board[column3.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif column3.index(dash) == 1:
            board[column3.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
        elif column3.index(dash) == 2:
            board[column3.index(dash) + 7] = logicPlayer
            checkWinner(currentPlayer)
    elif diagonal.count('O') == 2 and dash in diagonal:
        if diagonal.index(dash) == 0:
            board[diagonal.index(dash) + 1] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal.index(dash) == 1:
            board[diagonal.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal.index(dash) == 2:
            board[diagonal.index(dash) + 7] = logicPlayer
            checkWinner(currentPlayer)
    elif diagonal2.count('O') == 2 and dash in diagonal2:
        if diagonal2.index(dash) == 0:
            board[diagonal2.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal2.index(dash) == 1:
            board[diagonal2.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal2.index(dash) == 2:
            board[diagonal2.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
    # To prevent Player from Winning
    elif row1.count('X') == 2 and dash in row1:
        board[row1.index(dash)+ 1] = logicPlayer
        checkWinner(currentPlayer)
    elif row2.count('X') == 2 and dash in row2:
        board[row2.index(dash)+ 4] = logicPlayer
        checkWinner(currentPlayer)
    elif row3.count('X') == 2 and dash in row3:
        board[row3.index(dash)+ 7] = logicPlayer
        checkWinner(currentPlayer)
    elif column1.count('X') == 2 and dash in column1:
        if column1.index(dash) == 0:
            board[column1.index(dash) + 1] = logicPlayer
            checkWinner(currentPlayer)
        elif column1.index(dash) == 1:
            board[column1.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif column1.index(dash) == 2:
            board[column1.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
    elif column2.count('X') == 2 and dash in column2:
        if column2.index(dash) == 0:
            board[column2.index(dash) + 2] = logicPlayer
            checkWinner(currentPlayer)
        elif column2.index(dash) == 1:
            board[column2.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif column2.index(dash) == 2:
            board[column2.index(dash) + 6] = logicPlayer
            checkWinner(currentPlayer)
    elif column3.count('X') == 2 and dash in column3:
        if column3.index(dash) == 0:
            board[column3.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif column3.index(dash) == 1:
            board[column3.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
        elif column3.index(dash) == 2:
            board[column3.index(dash) + 7] = logicPlayer
            checkWinner(currentPlayer)
    elif diagonal.count('X') == 2 and dash in diagonal:
        if diagonal.index(dash) == 0:
            board[diagonal.index(dash) + 1] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal.index(dash) == 1:
            board[diagonal.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal.index(dash) == 2:
            board[diagonal.index(dash) + 7] = logicPlayer
            checkWinner(currentPlayer)
    elif diagonal2.count('X') == 2 and dash in diagonal2:
        if diagonal2.index(dash) == 0:
            board[diagonal2.index(dash) + 3] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal2.index(dash) == 1:
            board[diagonal2.index(dash) + 4] = logicPlayer
            checkWinner(currentPlayer)
        elif diagonal2.index(dash) == 2:
            board[diagonal2.index(dash) + 5] = logicPlayer
            checkWinner(currentPlayer)
    else:
        for k, v in board.items():
            if v == "-":
                emptyList.append(k)
            else:
                pass
        
        playerMove = random.choice(emptyList)
        # print (emptyList)
        # print (playerMove)
        # emptyList = []
        board[playerMove] = logicPlayer
        checkWinner(currentPlayer)


def addingToBoard(move):
    global currentPlayer
    global playerMove
    board[int(playerMove) - 1] = move
    checkWinner(currentPlayer)


def checkWinner(move):
    global currentPlayer
    global winner
    global board
    valid = True
    boardValues = list(board.values())

    # column = [(board[0, 3, 6]), (board[1, 4, 7]), (board[2, 5, 8])]
    # row = [(board[0, 1, 2]), (board[3, 4, 5]), (board[6, 7, 8])]
    # diagnoal = [(board[0, 4, 8]), (board[2, 4, 6])]

    while valid:
        if board[1] == board[2] == board[3] != dash or board[4] == board[5] == board[6] != dash or board[7] == board[8] == board[9] != dash or board[1] == board[4] == board[7] != dash:
            winner = True
            theWinner()
            break
        elif board[2] == board[5] == board[8] != dash or board[3] == board[6] == board[9] != dash or board[7] == board[5] == board[3] != dash or board[9] == board[5] == board[1] != dash:
            winner = True
            theWinner()
            break
        else:
            break
    if '-' not in boardValues:              # I have a Tie problrm here it does not work correctly!!!!!!!!!
        displayBoard()
        print("\n")
        print('Game over: It\'s a Tie  ')
        print("\n")
        playAgain()
        return
    else:
        flipPlayer(currentPlayer)


def theWinner():
    global currentPlayer
    displayBoard()
    print(f'The Winner is: {currentPlayer}')
    print("\n")
    playAgain()


def playAgain():
    global winner
    global board
    global l

    y_n = input('Would you like to play again? y/n: ')

    while y_n not in ['y', 'Y', 'n', 'N']:
        y_n = input('Choose "y" for yes or "n" for no: ')

    if y_n in ['y', 'Y']:
        board = {1: "-", 2: "-", 3: "-",
                 4: "-", 5: "-", 6: "-",
                 7: "-", 8: "-", 9: "-"}
        winner = False
        l = 0
        playGame()
    else:
        # winner = True
        print("\n")
        print('Thank you for playing fair!')
        return exit()


def flipPlayer(p):
    global currentPlayer
    if p == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
    return


def playGame():
    while winner == False:
        displayBoard()
        playerTurn()
    return


if __name__ == "__main__":
    playerName = input('You play with X, What is your Name? : ')
    playGame()
