class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i = row - 1
        j = 0

        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1      
            else:
                j += 1      

        return False