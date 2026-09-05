class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sm=0
        n=len(mat)
        for i in range(n):
            if i!=n-i-1:
                sm+=(mat[i][i]+mat[i][n-i-1])
            else:
                sm+=mat[i][i]
        return sm