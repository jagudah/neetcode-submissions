class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        lo, hi = 1, max(piles)
        res = float('inf')
        while lo <= hi:
            hrs = 0
            avg = (lo + hi) // 2
            for pile in piles:
                hrs += math.ceil(pile / avg)
            if hrs <= h:
                res = min(avg, res)
                hi = avg - 1
            else:
                lo = avg + 1
        return res