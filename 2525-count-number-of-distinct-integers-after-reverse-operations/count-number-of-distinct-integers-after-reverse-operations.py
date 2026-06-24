class Solution(object):
    def countDistinctIntegers(self, nums):
        n = len(nums)
        arr = []
        for i in range(n):
            rev = 0
            k = nums[i]
            while k!=0:
                d = k % 10
                rev = (rev*10) + d
                k //= 10
            arr.append(rev)

        for i in range(len(arr)):
            nums.append(arr[i])

        distinct = set(nums)
        return len(distinct)

