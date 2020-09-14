"""

https://leetcode.com/problems/search-in-rotated-sorted-array/

33. Search in Rotated Sorted Array (Medium)

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Edge check if rotated?
        
        
        
        left = 0
        right = len(nums) - 1
        
        #Binary Search
        while left <= right:
            mid = (left + right) // 2
            
            #Found
            if target == nums[mid]:
                return mid
            
            # nums[left to mid] is sorted 
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # nums[mid to right] is sorted
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                
        return -1