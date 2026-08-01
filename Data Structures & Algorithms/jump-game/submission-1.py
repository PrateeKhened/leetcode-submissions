class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0 

        for i in range(len(nums)):
            if i > far:
                return False 
            far = max(far, i + nums[i])
        return far >= len(nums) - 1