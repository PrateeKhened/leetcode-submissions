class Solution:
    def isValid(self, s: str) -> bool:
        dt = {"}": "{", ")": "(", "]": "["}
        st = [] 
        for c in s:
            if c not in dt:
                st.append(c)
            elif not st or dt[c] != st.pop():
                return False
        return len(st) == 0