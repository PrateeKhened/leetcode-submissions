class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = set()

        for num in nums:
            if num > 0:
                pos.add(num)
                
        if len(pos) == 0:
            return 1

        maxx = max(pos)
        for i in range(1, maxx):
            if i not in pos:
                return i

        return maxx + 1