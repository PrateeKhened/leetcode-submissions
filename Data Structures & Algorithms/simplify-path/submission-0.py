class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0 
        while i < len(path):
            string = ""
            if path[i] == "/":
                while i < len(path) and path[i] == "/":
                    i += 1
            else:
                while i < len(path) and path[i] != "/":
                    string += path[i]
                    i += 1 
            
            if string == ".":
                    continue 
            elif string == "..":
                if stack:
                    stack.pop() 
            elif string:
                stack.append(string)
        return "/" + "/".join(stack)