class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        t=[[0]*len(mat) for _ in range(len(mat[0]))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                t[j][i]=mat[i][j]
        return t
