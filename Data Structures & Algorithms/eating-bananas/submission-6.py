class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = float('inf')

        while l <= r:
            hours = 0
            speed = (l + r) // 2

            for pile in piles:
                hours += math.ceil(pile / speed)
            
            if hours <= h:
                result = min(result, speed)
                r = speed - 1
            else:
                l = speed + 1
        
        return result