class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        freq = {}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        for key in freq:
            if freq[key] >= 2:
                return True

        return False