class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        def dfs(u, v, visited):
            if u == v:
                return True 
            
            visited.add(u)

            for nei in g[u]:
                if nei not in visited:
                    if dfs(nei, v, visited):
                        return True 
            return False 

        for u, v in edges:
            visited = set() 

            if u  in g and v in g:
                if dfs(u, v, visited):
                    return [u, v]
            g[u].append(v)
            g[v].append(u)