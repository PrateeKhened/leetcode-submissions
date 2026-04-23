class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        left  = 1 
        for i in range(len(nums)):
            final.append(left)
            left *= nums[i]
        
        right = 1 
        for i in range(len(nums) - 1, -1 , -1):
            final[i] *= right 
            right *= nums[i]
        return final