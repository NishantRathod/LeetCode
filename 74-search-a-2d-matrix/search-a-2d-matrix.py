class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    return True
        return False