class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False 
        
        h = Counter(s1)
        n_h = Counter(s2[:n])

        if n_h == h:
            return True 
        
        for i in range(n, len(s2)):
            n_h[s2[i]] += 1

            n_h[s2[i - n]] -= 1
            if n_h == h:
                return True 
        return False