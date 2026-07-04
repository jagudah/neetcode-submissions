class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        nums = [-n for n in nums]

        heapq.heapify(nums)

        kLargestNums = heapq.nsmallest(k, nums)

        return (kLargestNums[k-1] * -1)