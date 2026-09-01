class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = {}
        countList = []

        for num in nums:
            if counter.get(num, 0) == 0:
                counter[num] = 0
            counter[num] -= 1
        
        for num in counter:
            countList.append([counter[num], num])
        
        heapq.heapify(countList)

        while k > 0:
            temp = heapq.heappop(countList)
            result.append(temp[1])
            k -= 1
        
        return result