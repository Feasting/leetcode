# 9-6-2020
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            p = p.children[c]
        p.end = True
        

    def search(self, word: str) -> bool:
        def helper(word, p):
            for i, letter in enumerate(word):
                if letter in p.children:
                    p = p.children[letter]
                else:
                    if letter == '.':
                        for key in p.children:
                            if helper(word[i+1:], p.children[key]):
                                return True
                    return False
            return p.end
        
        p = self.root
        return helper(word, p)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
