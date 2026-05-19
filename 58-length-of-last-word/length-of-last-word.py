class Solution(object):
    def lengthOfLastWord(self, s):
        n = len(s)
        cnt = 0
        for i in range(n-1,-1,-1):
            x = ord(s[i])
            if x == 32 and cnt==0:
                continue
            if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
                cnt += 1
            else:
                break
        return cnt