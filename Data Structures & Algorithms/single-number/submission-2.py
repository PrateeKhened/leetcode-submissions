class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dig = 0 
        for num in nums:
            dig ^= num 
        return dig