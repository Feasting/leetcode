# 9-13-2020
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) > len(t):
            return False
        p = 0
        for c in t:
            if c == s[p]:
                p += 1
                if p == len(s):
                    return True
        return False
