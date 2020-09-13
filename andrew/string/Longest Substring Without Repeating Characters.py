"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

#O(n) solution - generating all possible substrings - brute force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longestCount = 0
        
        index = 0
        i = 0
        currCount = 0
        set1 = set()
        while index <= len(s) - 1:
            if s[index] not in set1:
                set1.add(s[index])
                currCount += 1
            else:
                set1 = set()
                index = i
                currCount = 0
                i += 1
                        
            if currCount > longestCount:
                longestCount = currCount
            
            index += 1
            
        return longestCount


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Sliding Window
        
        longestCount = 0
        ptr1 = 0
        ptr2 = 0
        
        set1 = set()
        
        while ptr1 < len(s) and ptr2 < len(s):
            if s[ptr2] not in set1:
                set1.add(s[ptr2])
                ptr2 += 1
                longestCount = max(longestCount,  ptr2 - ptr1)
            else:
                set1.remove(s[ptr1])
                ptr1 += 1 
        
        return longestCount