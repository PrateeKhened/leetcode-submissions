class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates 
        n = len(nums)
        nums.sort() 

        res, sol = [], []

        def dfs(i, t):
            if t == 0:
                res.append(sol[:])
                return 
            
            if i >= n or t < 0 or nums[i] > t:
                return 
            
            sol.append(nums[i])
            dfs(i + 1, t - nums[i])
            sol.pop() 

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1 

            dfs(i + 1, t)
        
        dfs(0, target)
        return res