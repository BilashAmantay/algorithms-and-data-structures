def solution(matrix):
    row , col = len(matrix), len(matrix[0])
    total=0
    for c in range(col):
        for r in range(row):
            if matrix[r][c]==0:
                break
            total+=matrix[r][c]
    return total
            
            
matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]


print(solution(matrix))