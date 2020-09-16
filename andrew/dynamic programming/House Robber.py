"""

https://leetcode.com/problems/house-robber/

198. House Robber (Easy)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #Build upwards
        memo = [None] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            #Rob previous house then cant rob this house - so set next house to same as last
            #Rob two houses ago then can rob this house 
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i] )
        
        return memo[ len(nums)]

"""

#Rob House Zero
        dp[0] = 0
        #Rob House One
        dp[1] = dp[0] 
        
        for i in range(2, len(nums) + 1):
            #Robbed Last House
            robbedLastHouse = dp[i - 1]
            #Didn't Rob Last House, so add amt from two houses ago + current house
            didNotRobLastHouse = dp[i - 2] + nums[i - 1]
            dp[i] = max(robbedLastHouse, didNotRobLastHouse)
        
        #Return amount at last house where robbed or not
        return dp[ len(nums) ]

"""