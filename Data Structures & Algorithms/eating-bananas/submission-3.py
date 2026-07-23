class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        minSpeed = float('inf')

        while l <= r:
            speed = (l + r) // 2
            time = 0

            for pile in piles:
                time += math.ceil((pile / speed))
            if time <= h:
                minSpeed = min(minSpeed, speed)
                r = speed - 1
            else:
                l = speed + 1
        
        return minSpeed