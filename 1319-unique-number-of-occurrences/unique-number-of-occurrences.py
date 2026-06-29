class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1


        for key1 in freq:
            for key2 in freq:
                if key1 != key2 and freq[key1] == freq[key2]:
                    return False

        return True