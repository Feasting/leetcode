# 9-6-2020
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        size = len(s)
        count = {}
        for i in range(size):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            if t[i] in count:
                count[t[i]] -= 1
            else:
                count[t[i]] = -1
        
        for key in count:
            if count[key] != 0:
                return False
        
        return True

