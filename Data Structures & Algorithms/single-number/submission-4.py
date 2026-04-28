class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dig = 0 
        for n in nums:
            dig ^= n 
        return dig 