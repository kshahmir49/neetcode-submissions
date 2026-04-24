class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = nums[0]
        i = 1
        while i<len(nums):
            currsum = max(currsum+nums[i],nums[i])
            maxsum = max(maxsum,currsum)
            i += 1
        return maxsum