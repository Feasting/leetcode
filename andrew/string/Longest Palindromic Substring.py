"""

https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring (Medium)

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

#O(n^3) solution - Brute Force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestStr = ""
        set1 = set()
        
        for i in range(0, len(s)):
            tempStr = ""
            for j in range(i, len(s)):
                tempStr += s[j]
                
                if tempStr not in set1 and self.isPalindrome(tempStr):
                    set1.add(tempStr)
                    if len(tempStr) > len(longestStr):
                        longestStr = tempStr
        
        return longestStr
                    
    
    def isPalindrome(self, str1):
        return str1 ==  str1[::-1]
