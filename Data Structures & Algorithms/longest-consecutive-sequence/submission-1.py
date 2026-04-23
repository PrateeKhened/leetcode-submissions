class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        longest = 0 
        set_num = set(nums)

        for num in set_num:
            if num - 1 not in set_num:
                length = 1
                while num + length in set_num:
                    length += 1
                longest = max(longest, length)
        return longest