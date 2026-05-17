class Solution(object):
    def canReach(self, arr, start):

        n = len(arr)

        def dfs(i):

            if i < 0 or i >= n or arr[i] < 0:
                return False

            if arr[i] == 0:
                return True

            jump = arr[i]

            arr[i] = -arr[i]

            return dfs(i + jump) or dfs(i - jump)

        return dfs(start)