class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l = 1
        r = max(piles)
        minSpeed = piles[-1]

        while l <= r:
            speed = (l+r) // 2
            hours = 0

            for pile in piles:
                if (pile % speed) > 0:
                    hours += ((pile // speed) + 1)
                else:
                    hours += (pile // speed)
            
            if hours <= h:
                minSpeed = min(minSpeed, speed)
                r = speed - 1
            else:
                l = speed + 1
        
        return minSpeed