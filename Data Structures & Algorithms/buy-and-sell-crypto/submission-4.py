class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while l < len(prices) - 1:
            if prices[l] >= prices[r]:
                r += 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
            
            if r == len(prices):
                l += 1
                r = l + 1

        return res