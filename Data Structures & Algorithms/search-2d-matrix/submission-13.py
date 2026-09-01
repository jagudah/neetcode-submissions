class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, left = 0, 0
        bot, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if (target < matrix[mid][0]):
                bot = mid - 1
            elif (target > matrix[mid][-1]):
                top = mid + 1
            else:
                break
        
        while left <= right:
            m = (left + right) // 2

            if (target < matrix[mid][m]):
                right = m - 1
            elif (target > matrix[mid][m]):
                left = m + 1
            else:
                return True
        
        return False