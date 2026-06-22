class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        n = x
        sumOfNum = 0
        while n!=0:
            d = n % 10
            sumOfNum += d
            n //= 10
        if x % sumOfNum == 0:
            return sumOfNum
        return -1