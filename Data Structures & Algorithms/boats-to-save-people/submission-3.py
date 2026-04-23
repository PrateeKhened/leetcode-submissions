class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        total = 0 
        l, r = 0, len(people) - 1
        people.sort(reverse=True)
        while l <= r:
            if l < r and people[l] + people[r] <= limit:
                total += 1
                l += 1
                r -= 1
            else:
                total += 1
                l += 1
        return total