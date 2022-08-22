class Solution:
    def countSquares(self, matrix: int) -> int:
        if not matrix: return 0
        rows = len(matrix)
        columns = len(matrix[0])

        result = 0

        if rows ==0: return 0

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] ==1:
                    if row == 0 or column == 0:
                        result +=1
                    else:
                        cellVal = min(matrix[row-1][column-1], 
                                      matrix[row-1][column],
                                      matrix[row][column-1]) + matrix[row][column]
                        result += cellVal
                        matrix[row][column] = cellVal
        return result 




matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]                    
s = Solution()
print(s.countSquares(matrix))
