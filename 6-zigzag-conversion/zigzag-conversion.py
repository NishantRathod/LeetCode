class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]

        row = 0
        step = 1

        for ch in s:
            rows[row].append(ch)

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        ans = []

        for r in rows:
            ans.extend(r)

        return "".join(ans)