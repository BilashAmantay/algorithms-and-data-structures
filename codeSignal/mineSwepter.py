"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
the output should be

solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
Check out the image below for better understanding:
"""

def solution(matrix):
    
    rows, columns = len(matrix), len(matrix[0])
    res = []
    
    for r in range(rows):
        newRow = []
        for c in range(columns):
            cnt = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    ri = r+i
                    cj = c+j
                    if 0<=ri<rows and 0<=cj<columns and (ri!=r or cj!=c):
                        cnt+=matrix[ri][cj]
            newRow.append(cnt)
        res.append(newRow)
        
    return res
    
matrix = [[True,False,False], 
 [False,True,False], 
 [False,False,False]]                

print(solution(matrix))
