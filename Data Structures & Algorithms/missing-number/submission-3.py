class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1))// 2
        summ = 0 
        for n in nums:
            summ += n 
        return total - summ