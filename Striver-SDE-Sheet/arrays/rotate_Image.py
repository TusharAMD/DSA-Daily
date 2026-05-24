class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top_left_corner = 0
        bottom_right_corner = len(matrix)-1
        while top_left_corner<bottom_right_corner:
            for i in range(bottom_right_corner-top_left_corner):
                topleft=matrix[top_left_corner][top_left_corner+i]
                matrix[top_left_corner][top_left_corner+i]=matrix[bottom_right_corner-i][top_left_corner]
                matrix[bottom_right_corner-i][top_left_corner]=matrix[bottom_right_corner][bottom_right_corner-i]
                matrix[bottom_right_corner][bottom_right_corner-i]=matrix[top_left_corner+i][bottom_right_corner]
                matrix[top_left_corner+i][bottom_right_corner] = topleft
            top_left_corner+=1
            bottom_right_corner-=1


        