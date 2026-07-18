class Solution(object):
    def findGCD(self, nums):
        n = len(nums)
        largest = nums[0]
        smallest = nums[0]
        
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]

            if nums[i] < smallest:
                smallest = nums[i]

        divisor = 1
        for i in range(1,smallest+1):
            if smallest % i == 0 and largest % i == 0:
                divisor = i
        
        return divisor