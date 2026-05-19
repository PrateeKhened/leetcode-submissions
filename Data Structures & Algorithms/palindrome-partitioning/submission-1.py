class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [] ,[] 

        def dfs(i):
            if i == len(s):
                res.append(sol[:])
                return 
            
            for j in range(i, len(s)):
                sub = s[i : j + 1]
 
                if sub[::-1] == sub:
                    
                    sol.append(sub)

                    dfs(j + 1)

                    sol.pop() 
        
        dfs(0)
        return res