# 9-17-2020
# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        db = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        size = len(words)
        unique = set()
        for i in range(size):
            result = ''
            for c in words[i]:
                result += db[ord(c) - ord('a')]
            unique.add(result)
        return len(unique)
