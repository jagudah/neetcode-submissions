class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        result = []
        freqList = []
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        for num in counter:
            freqList.append([counter[num] * -1, num])
        
        heapq.heapify(freqList)

        while k > 0:
            elem = heapq.heappop(freqList)
            result.append(elem[1])
            k -= 1
        
        return result