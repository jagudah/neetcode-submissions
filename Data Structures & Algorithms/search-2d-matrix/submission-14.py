class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        listOne = []
        for row in matrix:
            listOne.extend(row)

        l, r = 0, len(listOne) - 1

        while l <= r:
            m = (l+r) // 2

            if (target < listOne[m]):
                r = m - 1
            elif (target > listOne[m]):
                l = m + 1
            else:
                return True
        
        return False