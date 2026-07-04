class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        while top <= bot:
            mRow = (top + bot) // 2

            if target < matrix[mRow][0]:
                bot = mRow - 1
            elif target > matrix[mRow][-1]:
                top = mRow + 1
            else:
                break
        
        if top > bot:
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        
        return False