class Solution(object):
    def isSameAfterReversals(self, num):
        n = num
        rev = 0
        while n!=0:
            d = n % 10
            rev = (rev*10) + d
            n //= 10
        x = rev
        newRev = 0
        while x!=0:
            d = x % 10
            newRev = (newRev*10) + d
            x //= 10
        if newRev == num:
            return True
        return False
