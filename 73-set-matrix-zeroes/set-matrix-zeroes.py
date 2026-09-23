class Solution(object):
    def setZeroes(self, matrix):
        row = set()
        column = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        for r in row:
            for i in range(0,n):
                matrix[r][i] = 0
        for c in column:
            for j in range(0,m):
                matrix[j][c] = 0






















        # row = set()
        # col = set()
        # for i in range(0,len(matrix)):
        #     for j in range(0,len(matrix[0])):
        #         if matrix[i][j]==0:
        #             row.add(i)
        #             col.add(j)
        # for r in row:
        #     for a in range(0,len(matrix[0])):
        #         matrix[r][a]=0
        # for c in col:
        #     for b in range(0,len(matrix)):
        #         matrix[b][c]=0
        