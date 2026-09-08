class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = float('inf')

        while lo <= hi:
            speed = (lo + hi) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile / speed)
            if count <= h:
                k = min(k, speed)
                hi = speed - 1
            else:
                lo = speed + 1
        return k