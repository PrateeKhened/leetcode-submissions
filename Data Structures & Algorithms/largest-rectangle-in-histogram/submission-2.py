class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0 

        for i, h in enumerate(heights):
            start = i 
            while st and st[-1][1] > h:
                index, height = st.pop() 
                res = max(res, height * (i - index))
                start = index 
            st.append((start, h))
        
        for i, h in st:
            res = max(res, h * (len(heights) - i))
        
        return res