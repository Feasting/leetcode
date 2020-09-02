# 9-2-2020
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        store = {}
        size = len(s)
        i = 0
        j = 0
        while j < size:
            if s[j] in store:
                i = max(store[s[j]], i)
            result = max(result, j - i + 1)
            store[s[j]] = j + 1
            j += 1
        return result
