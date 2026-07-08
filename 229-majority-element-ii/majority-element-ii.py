class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = {}
        ans = []

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for key in freq:
            if freq[key] > n / 3:
                ans.append(key)

        return ans