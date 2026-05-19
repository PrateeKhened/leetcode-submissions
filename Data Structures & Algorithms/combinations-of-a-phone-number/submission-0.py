class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return [] 

        d = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
             "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res, sol = [], [] 

        def dfs(i=0):
            if i == len(digits):
                res.append(''.join(sol))
                return 
            
            for c in d[digits[i]]:
                sol.append(c)
                dfs(i + 1)
                sol.pop()

        dfs() 
        return res