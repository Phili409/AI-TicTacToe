import random 
import pandas
import numpy

class TicTacToe:
    def __init__(self):
        self.board = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]

        self.moves = []
        self.bestMoveBoard = None
        self.valid = 0
        self.wBoard = [
                       
        [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
        ]
        , [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        , [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ]
        , [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0]
        ]
        , [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        , [
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ]
        , [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        , [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
        ]
    def Board(self):
        gameBoard = pandas.DataFrame(self.board)
        for index, row in gameBoard.iterrows():
            print('|'.join(str(x) for x in row))

    def AI_Move(self):
            bestMove = None
            bestBoard = None
            bestScore = 0
            for i, Move in enumerate(self.wBoard):
                score = 0
                for x in range(3):
                    for y in range(3):
                        if self.board[x][y] == 'X':
                            score += Move[x][y]
                        elif self.board[x][y] == 'O':
                            score -= Move[x][y]
                if score > bestScore:
                    bestScore = score
                    bestMove = i
                    bestBoard = Move
            self.bestMoveBoard = bestBoard
            bMove = self.bestMoveBoard
            if self.valid == 0:
                self.moves.append(self.board[1][1])
                self.board[1][1] = 'O'
            if self.valid >= 1 and self.valid < 9:
                stop_loop = False
                for x in range(3):
                    for y in range(3):
                        if bMove[x][y] == 1 and (self.board[x][y] != 'X' and self.board[x][y] != 'O'):
                            self.moves.append(self.board[x][y])
                            self.board[x][y] = 'O'
                            stop_loop = True
                            break
                    if stop_loop:
                        break
            if self.valid > 8:
                stop = False
                for x in range(3):
                    for y in range(3):
                        if self.board[x][y] != 'X' and self.board[x][y] != 'O':
                            self.moves = self.board[x][y]
                            self.board[x][y] = 'O'
                            stop = True
                            break
                    if stop:
                        break

    def Player(self):
        while True:
            promp = input("Pick a number between 0-8:\n")
            if not promp.isdigit():
                print('Please input a number...\nTry again!')
                continue
            promp = int(promp)
            if promp not in range(9):
                print('Invalid, Try again')
                continue
            if promp in self.moves:
                print('Invalid, Try again')
                continue
            player = promp
            self.moves.append(player)
            row = player // 3
            col = player % 3
            self.board[row][col] = 'X'
            break

    def checkWin(self):
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return row[0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return  self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        if len(self.moves) == 9:
            return 'Tie'
        return None
        
    def Play(self):
        print('Welcome')
        while True:
            self.AI_Move()
            self.Board()
            winner = self.checkWin()
            if winner is not None:
                self.Board()
                if winner == 'Tie':
                    print("Game Over, Tie")
                else:
                    print('Game Over')
                    print(f'{winner}, won!')
                break
            self.Player()
            winner = self.checkWin()
            if winner is not None:
                self.Board()
                if winner == 'Tie':
                    print("Game Over")
                    print('Tie!')
                else:
                    print('Game Over')
                    print(f'{winner}, won!')
                break
            self.valid += 2
Game = TicTacToe()
Game.Play()