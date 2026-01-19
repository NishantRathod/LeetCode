class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxWater = 0
        while i < j:
            width = j-i
            ht = min(height[i],height[j])
            currWater = width * ht
            maxWater = max(maxWater , currWater)
            if(height[i]<height[j]):
                i += 1
            else:
                j -= 1
        return maxWater