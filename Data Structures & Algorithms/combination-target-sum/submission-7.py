class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], [] 

        def dfs(i, t):
            if t == 0:
                res.append(sol[:])
                return 

            if i >= n or t < 0:
                return 
            
            sol.append(nums[i])
            dfs(i, t - nums[i])
            sol.pop() 

            dfs(i + 1, t)
        
        dfs(0, target)
        return res
