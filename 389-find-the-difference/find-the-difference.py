class Solution(object):
    def findTheDifference(self, s, t):
        n = len(s)
        m = len(t)

        ans = ""
        freq = {}
        for i in range(m):
            if t[i] not in freq:
                freq[t[i]] = 1
            else:
                freq[t[i]] += 1

        for i in range(n):
            if s[i] not in freq:
                return s[i]
            freq[s[i]] -= 1

        for key in freq:
            if freq[key] >= 1:
                ans = key
        return ans