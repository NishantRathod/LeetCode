class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}

        unique = sorted(set(arr))

        for i in range(len(unique)):
            rank[unique[i]] = i + 1

        ans = []

        for num in arr:
            ans.append(rank[num])

        return ans