class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        listOne = []
        for row in matrix:
            listOne.extend(row)

        for num in listOne:
            if num == target:
                return True
        return False