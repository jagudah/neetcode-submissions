class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxAmt = 0

        while l < r:
            if heights[l] <= heights[r]:
                currAmt = heights[l] * (r - l)
                maxAmt = max(maxAmt, currAmt)
                l += 1
            else:
                currAmt = heights[r] * (r - l)
                maxAmt = max(maxAmt, currAmt)
                r -= 1
        
        return maxAmt