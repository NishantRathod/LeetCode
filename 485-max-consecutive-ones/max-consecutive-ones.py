class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        conse = 0
        maxConse = 0
        for num in nums:
            if num == 1:
                conse += 1
                maxConse = max(maxConse,conse)
            else:
                conse = 0
        return maxConse
            
