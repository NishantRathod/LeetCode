class Solution(object):
    def reverse(self, x):
        flag = False

        if x < 0:
            flag = True

        x = abs(x)
        ans = 0

        while x != 0:
            d = x % 10
            ans = (ans * 10) + d
            x //= 10

        if flag == True:
            NegativeNum = ans - (ans * 2)

            if NegativeNum < -(2**31) or NegativeNum > (2**31 - 1):
                return 0

            return NegativeNum

        if ans > (2**31 - 1):
            return 0

        return ans