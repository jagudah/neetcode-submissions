class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = float('inf')

        while lo <= hi:
            mid = (lo + hi) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                k = min(k, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return k