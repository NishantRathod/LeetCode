class Solution(object):
    def dominantIndex(self, nums):
        n = len(nums)
        SecondLarge = float('-inf')
        FirstLarge = float('-inf')
        index = -1
        for i in range(n):
            if nums[i] > FirstLarge:
                SecondLarge = FirstLarge
                FirstLarge = nums[i]
                index = i
            elif nums[i]>SecondLarge:
                SecondLarge = nums[i]

        if FirstLarge >= 2 * SecondLarge:
            return index
        else:
            return -1