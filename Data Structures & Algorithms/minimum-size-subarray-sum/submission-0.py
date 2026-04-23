class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        total = 0 
        mini = float('inf')

        for j in range(len(nums)):
            total += nums[j]

            while total >= target:
                mini = min(mini, j - i + 1)
                total -= nums[i]
                i += 1
        
        return 0 if mini == float('inf') else mini