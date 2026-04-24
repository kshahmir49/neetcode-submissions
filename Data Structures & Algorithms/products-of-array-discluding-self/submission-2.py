class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        l_prefix = 1
        for i in range(len(nums)):
            left.append(l_prefix)
            l_prefix *= nums[i]
        r_prefix = 1
        for i in range(-1,-len(nums)-1,-1):
            right.insert(0,r_prefix)
            r_prefix *= nums[i]
        return [i*j for i,j in zip(left,right)]