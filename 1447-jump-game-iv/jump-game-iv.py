from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        mp = defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)

        q = deque([0])
        visited = set([0])

        steps = 0

        while q:
            size = len(q)

            for _ in range(size):
                idx = q.popleft()

                if idx == n - 1:
                    return steps

                neighbors = mp[arr[idx]] + [idx - 1, idx + 1]

                for nei in neighbors:
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

                mp[arr[idx]] = []

            steps += 1

        return -1