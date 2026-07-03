class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned = set(word.lower() for word in banned)

        freq = {}
        n = len(paragraph)
        startIdx = 0

        for i in range(n):
            if not paragraph[i].isalpha():
                if startIdx < i:
                    word = paragraph[startIdx:i].lower()
                    freq[word] = freq.get(word, 0) + 1
                startIdx = i + 1


        if startIdx < n:
            word = paragraph[startIdx:n].lower()
            freq[word] = freq.get(word, 0) + 1

        max_freq = 0
        result = ""

        for key in freq:
            if key not in banned and freq[key] > max_freq:
                max_freq = freq[key]
                result = key

        return result