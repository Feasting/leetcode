# 9-6-2020
# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            p = p.children[c]
        p.end = True
        

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            else:
                p = p.children[c]
        return p.end
        

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            else:
                p = p.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
