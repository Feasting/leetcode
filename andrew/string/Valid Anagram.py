"""

https://leetcode.com/problems/valid-anagram/

242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Use dictionaries to keep track of counts for each value
        #Then compare the dictionaries
        
        if len(s) != len(t):
            return False
        
        dictS = {}
        dictT = {}
        
        #Fill dictionaries with counts of characters
        for i in range(0, len(s)):
            if s[i] not in dictS:
                dictS[ s[i] ] = 1
            else:
                dictS[ s[i] ] += 1
                
            if t[i] not in dictT:
                dictT[ t[i] ] = 1
            else:
                dictT[ t[i] ] += 1
                
        if len(dictS) != len(dictT):
            return False
        
        #Compare dictionaries
        for key, value in dictS.items():
            if key not in dictT:
                return False
            elif dictT[ key ] != value:
                return False
            
        return True