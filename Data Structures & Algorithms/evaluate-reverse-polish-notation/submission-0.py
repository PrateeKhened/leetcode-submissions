class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "-+*/"
        st = []
        for t in tokens:
            if t in ops:
                a = st.pop() 
                b = st.pop() 
                if t == "+": st.append(a + b)
                elif t == "-": st.append(b - a)
                elif t == "*": st.append(a * b)
                else: st.append(int(b / a))
            else:
                st.append(int(t))
        return st[0]