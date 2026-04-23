class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        i = 0 
        j = len(height) - 1
        while i < j:
            m = min(height[i], height[j])
            dif = j - i
            tot = m * dif
            if tot > res:
                res = tot 
            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1
        return res
