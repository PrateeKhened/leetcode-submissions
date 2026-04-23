class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        while n > 1:
            binary += f"{n % 2}"
            n = n // 2
        binary += f"{n}"
        bina = binary[::-1]
        count = 0 
        for b in bina:
            if b == "1":
                count += 1
        return count