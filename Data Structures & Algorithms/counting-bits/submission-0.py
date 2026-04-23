class Solution:
    def countBits(self, n: int) -> List[int]:
        def numBits(n):
            c = 0 
            while n != 0:
                n &= (n - 1)
                c += 1
            return c 
        res = []
        for i in range(n + 1):
            res.append(numBits(i))
        return res