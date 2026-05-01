class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            mini = heights[i]
            for j in range(i,len(heights)):
                mini = min(mini,heights[j])
                area = max(area,mini*(j-i+1))
        return area