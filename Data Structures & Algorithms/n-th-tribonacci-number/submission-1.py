class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        zero = 0 
        one = 1 
        two = 1
        for i in range(3, n + 1):
            res = zero + one + two 
            zero = one 
            one  = two 
            two = res
        return two 