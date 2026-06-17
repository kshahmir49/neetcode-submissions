class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        while start <= end:
            row = int((start + end)//2)
            if target > matrix[row][-1]:
                start = row + 1
            elif target < matrix[row][0]:
                end = row - 1
            else:
                break
        # if not (start<=end):
        #     return False
        start, end = 0,len(matrix[row])-1
        while start <= end:
            target_row = int((start + end)//2)
            if target < matrix[row][target_row]:
                end = target_row - 1
            elif target > matrix[row][target_row]:
                start = target_row + 1
            else:
                return True
        return False


