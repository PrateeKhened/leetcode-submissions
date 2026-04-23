class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1
        while i < j:
            n = target - numbers[i]
            if numbers[j] > n:
                j -= 1
            elif numbers[j] < n:
                i += 1
            else:
                return [i+1, j+1]