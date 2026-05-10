class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0 
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res < -214748364 or (res == -214748364 and digit < -8)):
                return 0 
            
            if (res > 214748364 or (res == 214748364 and digit > 7)):
                return 0 
            
            res = (res * 10) + digit 
        
        return res