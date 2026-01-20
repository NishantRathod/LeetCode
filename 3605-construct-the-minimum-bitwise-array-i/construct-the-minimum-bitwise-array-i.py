class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
            else:
                temp = 1
                while (n & temp) > 0:
                    temp <<= 1
                ans.append(n - (temp >> 1))        
        return ans