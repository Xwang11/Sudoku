class Board:

    def __init__(self):
        board = [[0] * 9] * 9 
        validValues = {}
        for x in range(0,9):
            for y in range(0,9):
                validValues.update({(x,y):[]})
        self.board = board
        self.validValues = validValues

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

    def importBoard(self, m):
        self.board = m
    
    # Functions for solving the puzzle
    # Method: Brute force: 
    # 1. check what values are possible for a square
    # 2. If only one value if possible, plug in and iterate through entire matrix
    # 3. Repeat until solved
    # *Checking valid: Check column, row, then box [0-2][3-5][6-8]

    # Round to index of nearest box
    def roundBox(self, i):
        iRound = -1
        if (i<3):
            iRound = 0
        elif (i < 6):
            iRound = 3
        else:
            iRound = 6

        return iRound
    
    # Checks if box can contain given value
    def checkValid(self, x,y, value):
        valid = True
        # Check column
        for i in range(0,9):
            if (self.board[x][i] == value):
                valid = False
        
        # Check row
        for i in range(0,9):
            if (self.board[i][y] == value):
                valid = False
        
        # Check box
        for i in range(self.roundBox(x), self.roundBox(x) + 2):
            for j in range(self.roundBox(y), self.roundBox(y)+2):
                if self.board[i][j] == value:
                    valid = False
        
        return valid
    # checks if board is complete
    def checkComplete(self):
        for x in range(0,9):
            for y in range(0,9):
                if self.board[x][y] == False:
                    return False
        return True
    
    def solve(self):
        while True:
            self.printBoard()
            for x in range(0,9):
                for y in range(0,9):
                    if self.board[x][y] == 0:
                        list = self.validValues[(x,y)]

                        for i in range(1,10):
                            valid = self.checkValid(x, y, i)
                            if valid:
                                if i not in list:
                                    list.append(i)
                            elif not valid:
                                if i in list:
                                    list.remove(i)
                            
                            #print(f"x={x}, y={y}, i={i}, valid={valid}, list={list}")
                        if len(list) == 1:
                            self.board[x][y] = list[0]
                            
            if self.checkComplete():
                break