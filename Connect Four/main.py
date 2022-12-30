import os
import random
from settings import Settings
import AsciiArt
import time


winner = 0
playerturnloop = 1
gameloop = 2
invalidinput1 = 1
invalidinput2 = 1
invalidinput3 = 1
invalidinput4 = 1
invalidinput5 = 1
invalidinput6 = 1


while gameloop > 1:

    invalidinput6 = 1

    os.system('clear')

    s = Settings()

    board = []

    for i in range(s.height):
        list1 = []
        for j in range(s.width):
            list1.append('-')
        board.append(list1)

    def stringList(list):
        string = ''
        for i in range(len(list)):
            string += list[i]
        return string

    def checkWinner(list, tokenType):
        fourToken = tokenType*4

        # check horizontal
        for i in range(len(list)):
            row = list[i]
            strRow = stringList(row)
            if fourToken in strRow:
                if tokenType == s.player1:
                    global winner
                    global playerturnloop
                    winner += 1
                    playerturnloop += 1
                elif tokenType == s.player2:
                    winner = 0
                    playerturnloop = 1
                    winner += 2
                    playerturnloop += 1
                else:
                    print('Error')
                    time.sleep(1)
                    break
            
        # check vertical
        col = []
        for i in range(len(list) + 1):
            col = []
            for j in range(len(list)):
                row = list[j]
                col.append(row[i])

            strCol = stringList(col)
            if fourToken in strCol:
                if tokenType == s.player1:
                    winner += 1
                    playerturnloop += 1
                elif tokenType == s.player2:
                    winner = 0
                    playerturnloop = 1
                    winner += 2
                    playerturnloop += 1
                else:
                    print('Error')
                    time.sleep(1)
                    break

    def checkDiagonal(list, tokenType):
        y = 0
        x = 0
        point = 0
        try:
            for i in range(3):
                for i in range(4):
                    for i in range(4):
                        if list[y][x] == tokenType:
                            point += 1
                            if point == 4:
                                if tokenType == s.player1:
                                    global winner
                                    global playerturnloop
                                    winner += 1
                                    playerturnloop += 1
                                    return
                                elif tokenType == s.player2:
                                    winner = 0
                                    playerturnloop = 1
                                    winner += 2
                                    playerturnloop += 1
                                    return
                                else:
                                    print('Error')
                                    time.sleep(1)
                                    break
                            else:
                                pass
                            y += 1
                            x += 1
                        else:
                            point = 0
                            break
                    x += 1
                x = 0    
                y += 1
        
            y = 5
            x = 0
            point = 0
            for i in range(3):
                for i in range(4):
                    for i in range(4):
                        if list[y][x] == tokenType:
                            point += 1
                            if point == 4:
                                if tokenType == s.player1:
                                    winner += 1
                                    playerturnloop += 1
                                    return
                                elif tokenType == s.player2:
                                    winner = 0
                                    playerturnloop = 1
                                    winner += 2
                                    playerturnloop += 1
                                    return
                                else:
                                    print('Error')
                                    time.sleep(1)
                                    break
                            else:
                                pass
                            y -= 1
                            x += 1
                        else:
                            point = 0
                            break
                    x += 1
                x = 0
                y -= 1
        except:
            pass

    def printList(list):
        for i in range(len(list)):
            list1 = list[i]
            print('|', end='')
            for j in range(len(list1)):
                print(f" {list1[j]} ", end='')
            print('|')

    def dropToken(list, tokenType, x):
        y = 0
        while list[y][x] != '-':
            invalidinput5 = 1
            while invalidinput5 == 1:
                try:
                    os.system('clear')
                    printList(list)
                    column = int(input("That column was full, please enter a different column to drop your token in. "))
                    invalidinput5 += 1
                except:
                    os.system('clear')
                    print(AsciiArt.invalidinput)
                    time.sleep(1)
            if column in range(1, 8):
                column -= 1
                x = column
            os.system('clear')
            invalidinput5 -= 1
            
        i = 0
        while i < s.height:
            try:
                if list[y+1][x] == '-':
                    y += 1
                else:
                    list[y][x] = tokenType
                    break
            except IndexError:
                list[y][x] = tokenType
                break
            i += 1

    print(AsciiArt.connectfour)
    print("Press Enter to Play!")
    temp = input()
    os.system('clear')

    print(AsciiArt.chooseplayers)
    player10 = input("Type Player 1's Name: ")
    os.system('clear')
    print(player10 + " is using O's")
    time.sleep(2)
    os.system('clear')
    player20 = input("Type Player 2's Name: ")
    os.system('clear')
    print(player20 + " is using X's")
    time.sleep(2)
    os.system('clear')
    if random.randint(1,2) == 1:
        player1 = player10
        player2 = player20
    else:
        player1 = player20
        player2 = player10


    while playerturnloop == 1:
        while invalidinput1 == 1:
            while invalidinput3 == 1:
                os.system('clear')
                printList(board)
                try:
                    player1column = int(input(player1 + ", which column would you like to place your piece?: "))
                    invalidinput3 += 1
                except:
                    os.system('clear')
                    print(AsciiArt.invalidinput)
                    time.sleep(1)
            if player1column in range(1, 8):
                player1column -= 1
                invalidinput1 += 1
                dropToken(board, s.player1, player1column)
            else:
                os.system('clear')
                print(AsciiArt.invalidinput)
                time.sleep(1)
                invalidinput3 = 1

        os.system('clear')
        invalidinput1 = 1
        invalidinput3 = 1
        checkWinner(board, s.player1)
        checkDiagonal(board, s.player1)
        if playerturnloop == 1:
            pass
        else:
            break
        

        while invalidinput2 == 1:
            while invalidinput4 == 1:
                os.system('clear')
                printList(board)
                try:
                    player2column = int(input(player2 + ", which column would you like to place your piece?: "))
                    invalidinput4 += 1
                except:
                    os.system('clear')
                    print(AsciiArt.invalidinput)
                    time.sleep(1)
            if player2column in range(1, 8):
                player2column -= 1
                invalidinput2 += 1
                dropToken(board, s.player2, player2column)
                printList(board)

            else:
                os.system('clear')
                print(AsciiArt.invalidinput)
                time.sleep(1)
                invalidinput4 = 1

        os.system('clear')
        invalidinput2 = 1
        invalidinput4 = 1
        checkWinner(board, s.player2)
        checkDiagonal(board, s.player2)
        if playerturnloop == 1:
            pass
        else:
            break



    if winner == 1:
        print(AsciiArt.congrats)
        print(player1 + " is the winner!")
        time.sleep(2)
    elif winner == 2:
        print(AsciiArt.congrats)
        print(player2 + " is the winner!")
        time.sleep(2)
    else:
        print('Error')
        time.sleep(1)
        break

    
    while invalidinput6 == 1:  
        os.system('clear')
        print(AsciiArt.playagain)
        yn = input("Type y for yes or n for no: ")
        if yn == 'y':
            gameloop = 2
            playerturnloop = 1
            invalidinput1 = 1
            invalidinput2 = 1
            invalidinput3 = 1
            invalidinput4 = 1
            invalidinput5 = 1
            invalidinput6 = 0
            winner = 0
        elif yn == 'n':
            gameloop = 1
            invalidinput6 = 0
            os.system('clear')
        else:
            os.system('clear')
            print(AsciiArt.invalidinput)
            time.sleep(1)