class Solution(object):
    def maxArea(self, height):
        n = len(height)

        left = 0
        right = n - 1
        maxWater = 0
        while left < right:
            minHeight = min(height[left],height[right])
            width = right - left
            water = minHeight * width
            maxWater = max(water,maxWater)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
