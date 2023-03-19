class Board:
    board = []

    def __init__(self):
        board = [[0] * 9] * 9 
        self.board = board

    def __str__(self):
        boardString = "\n"
        for i in range(0,9):
            boardString = boardString + "{a} {b} {c} | {d} {e} {f} | {g} {h} {i} \n".format(
                a=self.board[i][0], 
                b=self.board[i][1],
                c=self.board[i][2],
                d=self.board[i][3],
                e=self.board[i][4],
                f=self.board[i][5],
                g=self.board[i][6],
                h=self.board[i][7],
                i=self.board[i][8],)
            if (i==2 or i==5):
                boardString = boardString + ("------  ------  ------\n")
        return boardString

    def printBoard(self):
        print(self.__str__())
