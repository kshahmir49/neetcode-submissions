class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # for i in range(0,len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        l,r=0,0
        res = []
        deq = []
        while r<len(nums):
            while deq and nums[deq[-1]]<nums[r]:
                deq.pop()
            deq.append(r)
            if l>deq[0]:
                deq.pop(0)
            if r-l+1 == k:
                res.append(nums[deq[0]])
                l+=1 
            r+=1
        return res