"""

https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs (Easy)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        #Count the number of ways to the top
        def climb(level, top, memo):
            if level == top:
                return 1
            elif level > top:
                return 0
            elif memo[level]:
                #Use previous computed value
                return memo[level]
            
            #Calculate how many steps recurvisely
            memo[level] = climb(level + 1, top, memo) + climb(level + 2, top, memo)
            
            return memo[level]
            
            
            
        memo = [None] * n
        return climb(0, n, memo)


#Iterative solution
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [None] * (n + 1)
        #Ways to climb 0 and 1 stairs is 1
        memo[0] = 1 
        memo[1] = 1
        for i in range(2, n + 1):
            #Two ways to get to next step which is take 1 or 2 steps
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]