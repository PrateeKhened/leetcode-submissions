class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, 0 
        ml = [0] * n 
        mr = [0] * n 

        for i in range(n):
            j = -i - 1
            ml[i] = l 
            mr[j] = r 
            l = max(l, height[i])
            r = max(r, height[j])
        
        summ = 0 
        for i in range(n):
            w = min(ml[i], mr[i])
            summ += max(0, w - height[i])
        
        return summ