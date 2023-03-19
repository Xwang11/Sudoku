class Board:
    board = []

    def __init__(self):
        board = [[0] * 9] * 9 
        self.board = board

    def __str__(self):
        boardString = ""
        for x in range(0,9):
            for y in range(0.9):
                boardString = boardString + board[x][y]
            boardString = boardString + "\n"
        return boardString

    def printBoard(self):
        for i in range(0,9):
            print(f"{board[i][0]} {board[i][1]} {board[i][2]} | {board[i][3]} {board[i][4]} {board[i][5]} | {board[i][6]} {board[i][7]} {board[i][8]} ")
            if (i==2 or i==5):
                print("------------------------------")
