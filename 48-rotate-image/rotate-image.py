class Solution(object):
    def rotate(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()



































        # for i in range(1,len(matrix)):
        #     for j in range(0,i):
        #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # for row in matrix:
        #     row.reverse()


        