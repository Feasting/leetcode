"""

https://leetcode.com/problems/implement-trie-prefix-tree/

208. Implement Trie (Prefix Tree) (Medium)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""

class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        index = 0
        currNode = self.root
        while index < len(word):
            if word[index] in currNode.children:
                #Traverse down Trie
                currNode = currNode.children[ word[index] ]
            else:
                #Create new path in Trie
                temp = TreeNode()
                currNode.children[ word[index] ] = temp
                currNode = temp
            
            index += 1
        #Indicate where it is the end of a word or not
        currNode.end = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        index = 0
        while index < len(word):
            if word[index] in currNode.children:
                #Traverse down Trie
                currNode = currNode.children[ word[index] ]
            else:
                return False
                
            index += 1
        
        if currNode.end == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        index = 0
        while index < len(prefix):
            if prefix[index] in currNode.children:
                #Traverse down Trie
                currNode = currNode.children[ prefix[index] ]
            else:
                return False
                
            index += 1
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)