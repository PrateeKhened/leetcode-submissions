class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x 
        res = 0 
        while l <= h:
            mid = l + ((h - l) // 2)
            if mid * mid < x:
                l = mid + 1
                res = mid 
            elif mid * mid > x:
                h = mid - 1
            else:
                return mid 
        return res