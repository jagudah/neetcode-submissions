class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = 0

        while row < len(matrix):
            if matrix[row][col] == target:
                return True
            col += 1

            if col == len(matrix[0]):
                row += 1
                col = 0
        
        return False