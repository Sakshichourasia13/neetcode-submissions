class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]:
        mat=[]
        if len(og)!=n*m:
            return []
        i=0
        while i<len(og):
            mat.append(og[i:i+n])
            i+=n
        return mat
