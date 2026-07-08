class Solution(object):
    def rearrangeArray(self, nums):
        ans = [0] * len(nums)

        positive = 0
        negative = 1

        for i in nums:
            if i > 0:
                ans[positive] = i
                positive += 2
            
            else:
                ans[negative] = i
                negative += 2
        
        return ans
        