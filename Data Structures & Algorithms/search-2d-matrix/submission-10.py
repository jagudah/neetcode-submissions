class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, l = 0, 0
        bot, r = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        while l <= r:
            m = (l + r) // 2

            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        
        return False