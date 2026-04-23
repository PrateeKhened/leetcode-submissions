class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(bin(n)[2:])
        n = 32 - len(binary)
        binary = "0" * n + binary
        return int(binary[::-1], 2)