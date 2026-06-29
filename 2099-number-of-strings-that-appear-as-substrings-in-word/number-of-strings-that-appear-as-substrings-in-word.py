class Solution(object):
    def numOfStrings(self, patterns, word):
        n = len(patterns)
        cnt = 0
        for i in range(n):
            if patterns[i] in word:
                cnt += 1
        return cnt
                