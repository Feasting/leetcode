# 9-9-2020
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        invert_store = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if c in invert_store:
                
                top = stack.pop() if stack else None

                if top != invert_store[c]:
                    return False
            else:
                stack.append(c)
        return not stack
