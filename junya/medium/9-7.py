class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        cur = []
        for char in s:
            if char in cur:
                cur = cur[cur.index(char)+1:]
            cur.append(char)
            ret = max(ret, len(cur))

        return ret
        
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
