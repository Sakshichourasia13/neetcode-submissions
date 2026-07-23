class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r=0
        has={}

        for i in grid:
            for j in i:
                if j in has:
                    r=j
                has[j]=1


        for i in range(1,(len(grid)**2)+1):
            if i not in has:
                return [r,i]