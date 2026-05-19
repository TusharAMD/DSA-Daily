class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0])
        m = len(matrix)
        row_list=[False]*m
        col_list=[False]*n
        for i in range(m):
            for j in range(n):
                #print(matrix[i][j])
                if matrix[i][j]==0:
                    row_list[i]=True
                    col_list[j]=True
        print(row_list)
        print(col_list)
        for i in range(m):
            for j in range(n):
                if row_list[i]==True or col_list[j]==True:
                    matrix[i][j]=0
