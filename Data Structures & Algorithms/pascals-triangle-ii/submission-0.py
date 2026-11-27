class Solution:
    def getRow(self, row: int) -> List[int]:
        t=[[1],[1,1]]
        if row<2:
            return t[row]

        i=2
        while i<=row:
            n=[1]
            j=0
            while j<len(t[i-1])-1:
                n.append(t[i-1][j]+t[i-1][j+1])
                j+=1
            if len(n)==i:
                n.append(1)
                t.append(n)
            i+=1
        return t[-1]
