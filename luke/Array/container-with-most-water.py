class Solution:
    def maxArea(self, height) -> int:
        maxHLeft = float("-inf")
        maxHRight = float("-inf")
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxHLeft = max(maxHLeft, height[left])
            maxHRight = max(maxHRight, height[right])
            if maxHLeft > maxHRight:
                area = maxHRight * (right - left)
                right -= 1
            else:
                area = maxHLeft * (right - left)
                left += 1
            maxArea = max(maxArea, area)
            
        return maxArea

    # cleaner
    def maxArea2(self, height) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            
        return maxArea