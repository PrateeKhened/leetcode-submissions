class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["*"] = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):

            if i == len(word):
                return "*" in node
            
            c = word[i]

            if c == ".":
                for k, v in node.items():
                    if k == "*":
                        continue 
                    if dfs(i + 1, v):
                        return True
                return False 
            
            if c not in node:
                return False 

            return dfs(i + 1, node[c])            

        return dfs(0, self.trie)