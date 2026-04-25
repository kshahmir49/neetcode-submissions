class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l,r = 0,len(heights)-1
        while l<r:
            max_water = max(max_water, (r-l)*min(heights[r],heights[l]))
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return max_water