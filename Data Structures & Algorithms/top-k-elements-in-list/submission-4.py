class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heapList = []
        result = []
        count = Counter(nums)
        
        for num in count:
            heapList.append([count[num] * -1, num])
        
        heapq.heapify(heapList)

        while k > 0:
            pair = heapq.heappop(heapList)
            result.append(pair[1])
            k -= 1
        
        return result