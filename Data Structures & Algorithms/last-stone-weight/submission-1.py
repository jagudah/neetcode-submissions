class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        if len(stones) == 1:
            return stones[0]
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            biggestStones = heapq.nsmallest(2, stones)
            weightDiff = biggestStones[0] - biggestStones[1]
            heapq.heappop(stones)
            heapq.heappop(stones)
            if weightDiff != 0:
                heapq.heappush(stones, weightDiff)
        
        return (stones[0] * -1) if len(stones) > 0 else 0