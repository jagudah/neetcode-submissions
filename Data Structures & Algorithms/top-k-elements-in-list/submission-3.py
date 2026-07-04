class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        numCount = defaultdict(int)
        numList = []
        result = []
        for num in nums:
            numCount[num] += 1
        
        for num in numCount:
            numList.append([numCount[num] * -1, num])
        
        heapq.heapify(numList)

        while k > 0:
            pair = heapq.heappop(numList)
            result.append(pair[1])
            k -= 1
        
        return result