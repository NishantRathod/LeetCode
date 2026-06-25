class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = 1
        return False