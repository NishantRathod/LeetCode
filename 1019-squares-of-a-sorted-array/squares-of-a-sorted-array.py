class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            sq = nums[i] * nums[i]
            ans.append(sq)

        ans.sort()
        return ans