class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            while st and st[-1] > 0 and a < 0:
                if st[-1] > abs(a):
                    a = 0
                    break 
                elif st[-1] < abs(a):
                    st.pop() 
                else:
                    
                    st.pop()
                    a = 0
                    break
            if a != 0 and (not st or st[-1] < 0 or a > 0):
                st.append(a)
        return st