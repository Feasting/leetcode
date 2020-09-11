"""

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

153. Find Minimum in Rotated Sorted Array (Medium)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #We can binary search through the array with two pointers
        #The two pointers update based on whether it is bigger than
        #the element at index 0 
		#Edge case
        if len(nums) == 1:
            return nums[0]
        
        leftPtr = 0
        rightPtr = len(nums) - 1
        
        #Check if there is rotation
        if nums[rightPtr] > nums[leftPtr]:
            #No rotation
            return nums[leftPtr]
        
        #Binary search
        while leftPtr <= rightPtr:
            
            mid = (leftPtr + rightPtr) // 2
            
            #Next value is decreasing then min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            #Element before is greater than this element is min
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            #Updates pointers to update mid to continue search
            if nums[mid] > nums[0]:
                leftPtr = mid + 1
            else:
                rightPtr = mid - 1