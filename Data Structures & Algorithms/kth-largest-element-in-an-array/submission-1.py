import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     nums[i] = -nums[i]
        # heapq.heapify(nums)
        # for _ in range(k-1):
        #     heapq.heappop(nums)
        # return -heapq.heappop(nums)

        res = []
        for i in nums:
            if len(res)<k:
                heapq.heappush(res,i)
            else:
                heapq.heappushpop(res,i)
        return res[0]
        