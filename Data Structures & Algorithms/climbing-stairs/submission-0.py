class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, memo={}):
            memo[1] = 1 
            memo[2] = 2 
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
            return memo[n]
        
        return helper(n)