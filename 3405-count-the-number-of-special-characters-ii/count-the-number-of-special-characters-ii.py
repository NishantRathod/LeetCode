class Solution(object):
    def numberOfSpecialChars(self, word):

        lower = {}
        upper = {}

        for i, ch in enumerate(word):

            if ch.islower():
                lower[ch] = i          

            else:
                if ch not in upper:
                    upper[ch] = i      

        cnt = 0

        for ch in lower:

            up = ch.upper()

            if up in upper and lower[ch] < upper[up]:
                cnt += 1

        return cnt