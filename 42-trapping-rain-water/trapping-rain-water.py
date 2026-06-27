class Solution(object):
    def trap(self, height):
        l_wall = r_wall = 0
        n = len(height)
        
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            max_left[i] = l_wall
            l_wall = max(l_wall,height[i])
        
        for j in range(n-1,-1,-1):
            max_right[j] = r_wall
            r_wall = max(r_wall,height[j])

        summ = 0
        for i in range(n):
            pot = min(max_left[i],max_right[i])
            summ += max(0,pot - height[i])
        return summ