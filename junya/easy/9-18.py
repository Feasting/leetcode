class Solution:
    def isValid(self, s: str) -> bool:
        ret = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                ret.append(char)
            else:
                if not ret:
                    return False
                check = ret.pop()
                if check == '(':
                    if char == '}' or char == ']':
                        return False
                elif check == '{':
                    if char == ')' or char == ']':
                        return False
                else:
                    if char == ')' or char == '}':
                        return False
        return not ret
        
# https://leetcode.com/problems/valid-parentheses/
