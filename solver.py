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
        
        # Check box BROKEN
        for y in range(self.roundBox(i), self.roundBox(i) + 2):
            for x in range(self.roundBox(j), self.roundBox(j)+2):
                if b[y][x] == k:
                    return False
        
        return True
    
    
    def solve(self,board, i, j):
        # board.printBoard()
        b=board.getBoard()
       

        if i >= 9:
            print("Complete")
            # board.printBoard()
            return True
        
        elif b[i][j] == 0:
            # print(f"Now checking ({i}, {j}) that has value {b[i][j]}")
            for k in range(1,10):
                if self.checkValid(board, i, j, k):
                    # print(f"({i}, {j}) can be solved with {k}")   
                    b[i][j] = k
                    board.setBoard(b)
                    if i==8 and j==8:
                        return True
                    if j==8:
                        iNew=i+1
                        jNew=0
                    else:
                        jNew = j + 1
                        iNew = i
                    
                    if self.solve(board,iNew,jNew):
                        return True
                    b[i][j] = 0
            return False

        else:
            # print(f"({i}, {j}) is not a blank space, incrementing")   
            if j==8:
                i=i+1
                j=0
            else:
                j=j+1
            return self.solve(board,i,j)