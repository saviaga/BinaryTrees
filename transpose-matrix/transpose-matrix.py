import numpy as np
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
           #x axis - > y axis
    #.    [0,0] [0,1][0,2]   [0,0][1,0][2,0]
     #    [[1,2,3],  [[1,4,7],
    #      [4,5,6],  [2,5,8],
    #      [7,8,9]]  [3,6,9]]
     #   
        
        cols = len(A[0])
        
        rows = len(A)
        print(rows),print(cols)
        new = [[0 for i in range(rows)] for i in range(cols)]
        
        for r in range(cols):
            for c in range(rows):
                new[r][c] = A[c][r]
        return new