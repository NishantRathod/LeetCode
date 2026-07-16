class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(self.gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        left, right = 0, n - 1

        while left < right:
            ans += self.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans