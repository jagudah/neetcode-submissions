class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        minSpeed = float('inf')

        while low <= high:
            speed = (low + high) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / speed)
            if time <= h:
                minSpeed = min(minSpeed, speed)
                high = speed - 1
            else:
                low = speed + 1
        
        return minSpeed