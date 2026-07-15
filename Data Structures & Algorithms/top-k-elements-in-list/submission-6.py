class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        res = []

        for num in nums:
            hashMap[num] = hashMap.get(num,0) - 1
        
        for num in hashMap:
            heap.append((hashMap[num], num))
        
        heapq.heapify(heap)

        while k > 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        return res