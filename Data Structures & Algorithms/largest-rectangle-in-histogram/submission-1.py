class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        # Brute force
        # for i in range(len(heights)):
        #     mini = heights[i]
        #     for j in range(i,len(heights)):
        #         mini = min(mini,heights[j])
        #         area = max(area,mini*(j-i+1))
        stack = []
        area = 0
        for i,j in enumerate(heights):
            index = i
            while stack and stack[-1][1] > j:
                index, height = stack.pop()
                area = max(area, height*(i-index))
            stack.append((index,j))
        for i,j in stack:
            area = max(area, j*(len(heights)-i))

        return area