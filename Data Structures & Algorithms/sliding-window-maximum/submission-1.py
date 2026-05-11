class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums and len(nums) < k:
            return []
        res = []
        l, r = 0, k
        while l < len(nums) and r <= len(nums) and l < r:
            res.append(max(nums[l:r])) 
            l += 1
            r += 1
        return res
        