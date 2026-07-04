class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        heapList = []
        result = []

        for num in nums:
            hashMap[num] -= 1
        
        for key in hashMap:
            heapList.append((hashMap[key], key))
        
        heapq.heapify(heapList)

        while k > 0:
            temp = heapq.heappop(heapList)
            result.append(temp[1])
            k -= 1
        
        return result