class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        result = []
        topKList = []
        numCount = Counter(nums)
        for num in numCount:
            result.append([numCount[num], num])
        heapq.heapify(result)
        
        topK = heapq.nlargest(k, result)
        for pair in topK:
            topKList.append(pair[1])
        return topKList