class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            bigStone = heapq.heappop(stones)
            smallStone = heapq.heappop(stones)
            heapq.heappush(stones, bigStone - smallStone)
        return 0 if not stones else heapq.heappop(stones) * -1