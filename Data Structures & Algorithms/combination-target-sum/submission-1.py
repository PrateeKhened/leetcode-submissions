class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(s, c, t):
            if t == target:
                res.append(c.copy())
                return 
            if t > target:
                return 
            for i in range(s, len(nums)):
                c.append(nums[i])
                backtrack(i, c, t + nums[i])
                c.pop() 
        backtrack(0, [], 0)
        return res