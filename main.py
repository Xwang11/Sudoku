from boardNew import Board
from solver import Solver
import time
b = Board()
s = Solver()

# Easy problem
m = [[9,2,0,0,0,5,8,0,0],
     [0,0,1,7,2,6,3,0,9],
     [0,0,3,8,9,1,2,0,6],
     [0,8,0,0,0,0,1,0,2],
     [7,0,0,0,6,0,5,0,8],
     [0,0,0,0,3,0,7,0,0],
     [5,0,8,0,1,3,0,0,7],
     [0,4,0,6,0,7,9,1,5],
     [0,0,0,2,0,0,6,0,0]
     ]
# m = [[5,2,7,6,1,3,4,8,9],
#      [1,8,6,9,7,4,2,3,5],
#      [4,9,3,5,8,2,6,7,1],
#      [2,7,1,4,9,6,8,5,3],
#      [9,6,5,2,3,8,7,1,4],
#      [3,4,8,1,5,7,9,6,2],
#      [6,1,2,7,4,5,3,9,8],
#      [8,5,4,3,6,9,1,2,7],
#      [7,3,9,8,2,1,5,4,0]
#      ]

# Evil lv problem - cannot solve brute force method
n = [[0,2,0,0,1,0,0,8,0],
     [0,0,6,0,0,0,0,3,0],
     [4,0,0,5,0,0,6,0,1],
     [0,7,0,4,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,0],
     [0,0,8,0,5,0,9,0,2],
     [0,0,0,0,0,0,3,0,0],
     [8,0,0,0,0,9,0,0,0],
     [0,0,9,0,2,0,5,0,6]]

start = time.perf_counter()
b.setBoard(n)
print(s.roundBox(8))
s.solve(b, 0, 0)
end = time.perf_counter()
print(end-start)
# b.printBoard()





