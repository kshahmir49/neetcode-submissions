class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        for i in range(len(nums)):
            prod = 1
            for j in range(i+1,len(nums)):
                prod *= nums[j]
            left.append(prod)
        
        for i in range(-1,-len(nums)-1,-1):
            prod = 1
            for j in range(i-1,-len(nums)-1,-1):
                prod *= nums[j]
            right.insert(0,prod)

        res = []
        for i,j in zip(left,right):
            res.append(i*j)
        return res         