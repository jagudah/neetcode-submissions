class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = float('inf')

        while l <= r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            if time <= h:
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1

        return k