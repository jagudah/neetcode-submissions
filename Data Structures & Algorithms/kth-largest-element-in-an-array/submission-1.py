class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        while k > 0:
            result = heapq.heappop(nums) * -1
            k -= 1
        return result