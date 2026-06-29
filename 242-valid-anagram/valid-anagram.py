class Solution(object):
    def isAnagram(self, s, t):
        n = len(s)
        m = len(t)

        freq = {}
        if n != m:
            return False

        for i in range(n):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1

        for i in range(m):
            if t[i] not in freq:
                return False
 
            freq[t[i]] -= 1

            if freq[t[i]] < 0:
                return False


        return True