"""

https://leetcode.com/problems/palindromic-substrings/

647. Palindromic Substrings (Medium)

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        self.count = 0
        #For each palindrome center, expand
        
        
        
        def expandMiddle(left, right, s):
            if left > right: return 0;
            
            #Left and right start at same center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            #Handle two different cases
                #Middle is center
            expandMiddle(i, i, s)
                #Two characters is center
            expandMiddle(i, i+1, s)
            
        return self.count