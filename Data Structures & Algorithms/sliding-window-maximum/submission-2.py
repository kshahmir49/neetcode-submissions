class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0,len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res