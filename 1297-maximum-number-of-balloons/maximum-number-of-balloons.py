class Solution(object):
    def maxNumberOfBalloons(self, text):
        freq = {}

        for ch in text:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )