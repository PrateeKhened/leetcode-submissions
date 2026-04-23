class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set() 

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for i in range(len(nums)):
                if i in seen:
                    continue 
                
                seen.add(i)
                curr.append(nums[i])

                dfs(curr)

                curr.pop() 
                seen.remove(i)
        dfs([])
        return res