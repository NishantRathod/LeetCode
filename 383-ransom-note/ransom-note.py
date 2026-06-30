class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        n = len(magazine)
        m = len(ransomNote)
        freq = {}

        for i in range(n):
            if magazine[i] not in freq:
                freq[magazine[i]] = 1
            else:
                freq[magazine[i]] += 1
        
        for i in range(m):
            if ransomNote[i] not in freq:
                return False

            freq[ransomNote[i]] -= 1

            if freq[ransomNote[i]] < 0:
                return False
        return True
        