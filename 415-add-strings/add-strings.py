class Solution(object):
    def addStrings(self, num1, num2):
        n = len(num1)
        m = len(num2)

        i = n - 1
        j = m - 1

        carry = 0
        ans = ""

        while i >= 0 and j >= 0:
            d1 = ord(num1[i]) - ord('0')
            d2 = ord(num2[j]) - ord('0')

            lastDigit = (d1 + d2 + carry) % 10
            ans += str(lastDigit)
            carry = (d1 + d2 + carry) // 10

            i -= 1
            j -= 1

        while i >= 0:
            d1 = ord(num1[i]) - ord('0')

            lastDigit = (d1 + carry) % 10
            ans += str(lastDigit)
            carry = (d1 + carry) // 10

            i -= 1

        while j >= 0:
            d2 = ord(num2[j]) - ord('0')

            lastDigit = (d2 + carry) % 10
            ans += str(lastDigit)
            carry = (d2 + carry) // 10

            j -= 1

        if carry > 0:
            ans += str(carry)

        return ans[::-1]