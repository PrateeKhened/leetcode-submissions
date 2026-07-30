class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = [] 
        n = len(nums) 
        def dfs(i, total):
            if i >= n or total < 0:
                return 
            if total == 0:
                res.append(sol[:])
                return 

            sol.append(nums[i])
            dfs(i, total - nums[i])
            sol.pop() 

            dfs(i + 1, total)
        dfs(0, target)
        return res