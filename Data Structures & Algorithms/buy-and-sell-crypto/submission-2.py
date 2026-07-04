class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        p1, p2 = 0, 1

        while p2 < len(prices):
            diff = prices[p2] - prices[p1]
            maxProfit = max(diff, maxProfit)

            if p2 < len(prices) - 1:
                p2 += 1
            else:
                p1 += 1
                p2 = p1 + 1
        
        return maxProfit