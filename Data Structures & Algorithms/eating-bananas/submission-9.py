class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, hi = 1, max(piles)
        k = float('inf')

        while low <= hi:
            speed = (low + hi) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)
            if hours <= h:
                k = min(k, speed)
                hi = speed - 1
            else:
                low = speed + 1
        
        return k