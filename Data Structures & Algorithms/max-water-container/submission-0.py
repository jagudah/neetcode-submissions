class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while l < (len(heights) - 1):
            # if heights[l] == 0:
            #     l += 1
            #     r = l + 1
            # elif heights[r] == 0:
            #     r += 1
            # else:
            volume = min(heights[l], heights[r]) * (r-l)
            res = max(res, volume)

            if r == (len(heights) - 1):
                l += 1
                r = l
            r += 1
        
        return res