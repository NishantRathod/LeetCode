class Solution(object):
    def reverseVowels(self, s):
        n = len(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]


        vowelString = ""
        for i in range(n):
            if s[i] in vowels:
                vowelString += s[i]

        ansString = ""
        lastIdx = len(vowelString) - 1


        for i in range(n):
            if s[i] in vowels:
                ansString += vowelString[lastIdx]
                lastIdx -= 1
            else:
                ansString += s[i]

        return ansString