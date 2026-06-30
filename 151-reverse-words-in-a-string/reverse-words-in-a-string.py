class Solution(object):
    def reverseWords(self, s):
        words = []
        word = ""

        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        ans = ""

        for i in range(len(words)):
            ans += words[i]
            if i != len(words) - 1:
                ans += " "

        return ans