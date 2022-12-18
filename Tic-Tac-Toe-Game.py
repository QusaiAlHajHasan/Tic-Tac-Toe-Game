import random
from array import *
class TicTacToe:
        def __init__(self):
                self.__board = [['','',''],['','',''],['','','']]
                self.__letter1='X'
                self.__letter2='O'
		
        def DrawBoard(self):
                print('    |    |    ')
                print(' ' + self.__board[0][0] + '    ' + self.__board[0][1] + '    ' + self.__board[0][2])
                print('    |    |    ')
                print('---------------')
                print('    |    |    ')
                print(' ' + self.__board[1][0] + '    ' + self.__board[1][1] + '    ' + self.__board[1][2])
                print('    |    |    ')
                print('---------------')
                print('    |    |    ')
                print(' ' + self.__board[2][0] + '    ' + self.__board[2][1] + '    ' + self.__board[2][2])
                print('    |    |    ')
        def ClearBoard(self):
                for i in range(0,3):
                        for j in range(0,3):
                                self.__board[i][j] = ''
        def CheckWin(self,l):
                return ((self.__board[0][0] == l and self.__board[0][1] == l and self.__board[0][2] == l) or
                        (self.__board[1][0] == l and self.__board[1][1] == l and self.__board[1][2] == l) or
                        (self.__board[2][0] == l and self.__board[2][1] == l and self.__board[2][2] == l) or
                        (self.__board[0][0] == l and self.__board[1][0] == l and self.__board[2][0] == l) or
                        (self.__board[0][1] == l and self.__board[1][1] == l and self.__board[2][1] == l) or
                        (self.__board[0][2] == l and self.__board[1][2] == l and self.__board[2][2] == l) or
                        (self.__board[0][0] == l and self.__board[1][1] == l and self.__board[2][2] == l) or
                        (self.__board[0][2] == l and self.__board[1][1] == l and self.__board[2][0] == l))
	
        def IsIndexFree(self , x , y):
                if x<=2 and x>=0 and y<=2 and y>=0:
                        if self.__board[x][y] == '':
                                return True
                return False
        def NewGame(self):
                print('Do Want To Play Again (Y : Yes , N : No) :')
                return input().lower()
        def WhoFirstPlayer(self):
                if random.randint(0,1) == 0:
                        self.__letter1 == 'X'
                        self.__letter2 == 'O'
                        return 'Player X'
                else:
                        self.__letter1 == 'O'
                        self.__letter2 == 'X'
                        return 'Player O'
        def CheckDraw(self):
                for i in range(0,3):
                        for j in range(0,3):
                                if self.IsIndexFree(i,j):
                                        return False
                                return True
        def GetPlayerMove(self,l):
                print('player ',l ,', Enter your move (row[0-2] column[0-2]):')
                x , y = input().split()
                return x , y
        def MakeMove(self , x , y, l):
                self.__board[x][y] = l
               
        def Play(self):
                turn_num =1
                loop = True
                while loop:
                        if turn_num % 2 !=0 :
                                a , b = self.GetPlayerMove(self.__letter1)
                                while not self.IsIndexFree(int(a) , int(b) ):
                                        print('This move is not valid. Try again…')
                                        a , b = self.GetPlayerMove(self.__letter1)
                                self.MakeMove(int(a) , int(b) , self.__letter1)
                                self.DrawBoard()
                                turn_num +=1
			
                        else :
                                a , b = self.GetPlayerMove(self.__letter2)
                                while not self.IsIndexFree(int(a) , int(b) ):
                                        print('This move is not valid. Try again…')
                                        a , b = self.GetPlayerMove(self.__letter2)
                                self.MakeMove(int(a) , int(b) , self.__letter2)
                                self.DrawBoard()
                                turn_num +=1
                                
                        if turn_num > 9 or self.CheckWin(self.__letter1) or self.CheckWin(self.__letter2) :
                                loop = False
                if self.CheckWin(self.__letter1):
                        print('Player ',self.__letter1 ,' Won.')
                elif self.CheckWin(self.__letter2):
                        print('Player ',self.__letter2 ,' Won.')
                else :
                        print('Tied')


                        
		
def main():
						
        Game1 = TicTacToe()
        while True:
                print('Welcome To Tic Tac Toe !')
                turn = Game1.WhoFirstPlayer()
                Game1.Play()
                ans = Game1.NewGame()
                if ans == 'y':
                        Game1.ClearBoard()
                        continue
                else:
                        print('Thank You !')
                        break

main()
	
