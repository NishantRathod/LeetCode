class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):

            if i - minJump >= 0:
                reachable += dp[i - minJump]

            if i - maxJump - 1 >= 0:
                reachable -= dp[i - maxJump - 1]

            if reachable > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]