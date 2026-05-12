class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        for i in range(0,n-1):
            j = i+1
            nums[j] = nums[i]+nums[j]
        return nums