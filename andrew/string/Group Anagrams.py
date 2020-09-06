"""

https://leetcode.com/problems/group-anagrams/

49. Group Anagrams (Medium)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	#Group anagrams, store dictionaries of anagrams in list
    	#Use the list of anagrams to determine what bucket to put the anagram into
    	#Complexity is bad because will have to search the list for every string
    	# O(n^2) time complexity, if we can somehow use set instead, we can make it O(n)        
        output = {}
        listDicts = []
        
        
        def createDict(s):
            dict1 = {}
            for i in s:
                if i not in dict1:
                    dict1[i] = 1
                else:
                    dict1[i] += 1
            return dict1
            
        for string in strs:
            anaDict = createDict(string)
            
            if anaDict not in listDicts:
                listDicts.append( anaDict )
                output[ len(listDicts) - 1 ] = [string] 
            else:
                index = listDicts.index(anaDict)
                output[ index ].append(string)
            
        return output.values()