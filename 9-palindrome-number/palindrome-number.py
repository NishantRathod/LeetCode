class Solution(object):
    def isPalindrome(self, x):
        n = x
        rev = 0
        while(n>0):
            d = n % 10
            rev = (rev*10) + d
            n //= 10
        if x == rev:
            return True
        return False
        