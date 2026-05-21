class Solution(object):
    def countGoodSubstrings(self, s):
        n = len(s)
        cnt = 0
        for i in range(n-2):
            j = i+1
            k = j+1
            if s[i]!= s[j] and s[j] != s[k] and s[i] != s[k]:
                cnt += 1
        return cnt