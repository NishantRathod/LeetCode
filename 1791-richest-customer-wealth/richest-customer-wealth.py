class Solution(object):
    def maximumWealth(self, accounts):
        ans = 0
        for i in range(len(accounts)):
            addition = 0
            for j in range(len(accounts[i])):
                addition += accounts[i][j]

            ans = max(addition,ans)
        return ans