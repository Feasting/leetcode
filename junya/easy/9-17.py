class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
# https://leetcode.com/problems/palindrome-number/
