class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            tempArea = 0

            if heights[l] < heights[r]:
                tempArea = heights[l] * (r - l)
                res = max(res, tempArea)
                l += 1
            else:
                tempArea = heights[r] * (r - l)
                res = max(res, tempArea)
                r -= 1
        
        return res