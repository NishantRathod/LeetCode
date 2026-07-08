class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        arr1 = []
        arr2 = []
        ans = []
        for i in nums:
            if i > 0:
                arr1.append(i)

            if i < 0:
                arr2.append(i)

        maxsize = max(len(arr1),len(arr2))

        for i in range(maxsize):
            if i < len(arr1): 
                ans.append(arr1[i])

            if i < len(arr2):
                ans.append(arr2[i])

        return ans