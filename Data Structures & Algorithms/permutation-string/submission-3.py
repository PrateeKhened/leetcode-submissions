class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1c = [0] * 26 
        s2c = [0] * 26 

        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1)):
            if s1c == s2c:
                return True 
            s2c[ord(s2[i]) - ord('a')] -= 1
            s2c[ord(s2[i + len(s1)]) - ord('a')] += 1
        return s1c == s2c