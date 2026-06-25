class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1)
        m = len(word2)
        ans = ""
        k = max(n,m)
        for i in range(k):
            if i < n:
                ans += word1[i]
            if i < m:
                ans += word2[i]
        return ans