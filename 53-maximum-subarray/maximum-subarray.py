class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        currMax = nums[0]
        maxSum = nums[0]
        for i in range(1,n):
            currMax = max(currMax + nums[i], nums[i])
            maxSum = max(currMax , maxSum)
        return maxSum