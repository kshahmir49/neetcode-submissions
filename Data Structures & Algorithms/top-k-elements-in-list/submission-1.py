class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for _ in range(len(nums)+1)]
        d = {}
        for i in nums:
            d[i] = 1+d.get(i,0)
        for a,b in d.items():
            for i in range(len(l)):
                if b==i:
                    l[i].append(a)
        res = []
        for i in range(len(l)-1,-1,-1):
            for j in l[i]:
                res.append(j)
                if len(res)==k:
                    return res