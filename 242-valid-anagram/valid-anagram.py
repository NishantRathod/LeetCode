class Solution(object):
    def isAnagram(self, s, t):
        n = len(s)
        m = len(t)

        if n != m:
            return False

        freqS = {}

        for i in range(n):
            if s[i] not in freqS:
                freqS[s[i]] = 1
            else:
                freqS[s[i]] += 1

        for i in range(m):
            if t[i] not in freqS:
                return False

            freqS[t[i]] -= 1

            if freqS[t[i]] < 0:
                return False

        return True