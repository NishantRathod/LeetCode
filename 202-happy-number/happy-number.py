class Solution(object):
    def isHappy(self, n):
        while n!=1:
            ans = 0
            while n!=0:
                d = n % 10
                sq = d * d
                ans += sq
                n //= 10
            n = ans
            if n==4:
                return False
        return True