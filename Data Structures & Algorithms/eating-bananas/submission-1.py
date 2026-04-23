class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (right + left) // 2
            duration = self.findtime(mid, piles)
            if duration > h:
                left = mid + 1
            else:
                right = mid - 1
        return left 

    def findtime(self, num, piles):
            total = 0 
            for n in piles:
                total += math.ceil(n / num)
            return total