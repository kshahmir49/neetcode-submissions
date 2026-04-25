class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) space but O(n^2) time
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]
        #         elif numbers[i] + numbers[j] > target:
        #             break  

        # O(n) space and O(n) time
        d = {}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[target-numbers[i]] = i+1
            else:
                return [d[numbers[i]],i+1] 