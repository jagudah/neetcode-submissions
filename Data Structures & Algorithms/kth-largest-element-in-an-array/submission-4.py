class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        while k > 0:
            temp = heapq.heappop(nums) * -1
            k -= 1
        return temp