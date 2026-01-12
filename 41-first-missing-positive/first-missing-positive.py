class Solution(object):
    def firstMissingPositive(self, arr):
        n = len(arr)
        flag = False

        for i in range(n):
            if arr[i] == 1:
                flag = True
                break

        if not flag:
            return 1

        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 1

        for i in range(n):
            arr[(arr[i] - 1) % n] += n

        for i in range(n):
            if arr[i] <= n:
                return i + 1
        return n + 1
        