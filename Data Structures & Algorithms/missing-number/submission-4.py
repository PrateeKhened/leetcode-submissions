class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1))// 2
        summ = 0 
        for num in nums:
            summ += num 
        return total - summ