class Solution:
    def decodeString(self, s: str) -> str:
        st = [] 
        num = 0 
        string = ""

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                st.append((num, string))
                string = ""
                num = 0 
            elif c == ']':
                p = st.pop()
                string = p[1] + p[0] * string
            else: 
                string += c 
        return string 
        