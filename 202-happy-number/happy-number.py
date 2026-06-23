class Solution(object):
    def isHappy(self, n):
        arr = []
        
        while n not in arr:
            arr.append(n)

            total = 0
            x = n

            while x > 0:
                d = x % 10
                total += d * d
                x //= 10

            if total == 1:
                return True

            n = total

        return False