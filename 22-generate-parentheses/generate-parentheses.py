class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def myParen(ans, left, right):
            if left == n and right == n:
                result.append(ans)
                return

            if left < n:
                myParen(ans + "(", left + 1, right)

            if right < left:
                myParen(ans + ")", left, right + 1)

        myParen("", 0, 0)
        return result