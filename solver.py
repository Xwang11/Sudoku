#Constructor, no parameters
#Solve(board)
#RoundBox(i)
#CheckValid(board, i, j, k)

class Solver:

    def __init__(self):
        pass

    def roundBox(self,i):
        answer = -1
        if (i<3):
            answer = 0
        elif (i < 6):
            answer = 3
        else:
            answer = 6

        return answer
    
    def checkValid(self,board, i, j, k):
        b=board.getBoard()

        # Check row
        for x in range(0,9):
            if (b[i][x] == k):
                return False
        
        # Check column
        for x in range(0,9):
            if (b[x][j] == k):
                return False
        
        # Check box
        for y in range(self.roundBox(i), self.roundBox(i) + 2):
            for x in range(self.roundBox(j), self.roundBox(j)+2):
                if b[y][x] == k:
                    return False
        
        return True
    
    def solve(self,board, i, j):
        board.printBoard()
        print(f"Now checking ({i}, {j})")
        b=board.getBoard()

        if i == 8 and j == 8:
            print("Complete")
            return True
        
        elif b[i][j] == 0:
            for k in range(1,10):
                if self.checkValid(board, i, j, k):
                    print(f"({i}, {j}) can be solved with {k}")   
                    b[i][j] = k
                    board.setBoard(b)
                    if i==8:
                        j=j+1
                        i=1
                    else:
                        i = i+1
                    
                    self.solve(board,i,j)

        else:
            print(f"({i}, {j}) is not a blank space, incrementing")   
            if i==8:
                j=j+1
                i=1
            else:
                i=i+1
            self.solve(board, i, j)