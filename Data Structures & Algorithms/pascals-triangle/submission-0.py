class Solution:
    def generate(self, n: int) -> List[List[int]]:
        a=[[1]]
        if n==1:
            return a
        for i in range(1,n):
            t=[1]
            for j in range(1,i):
                t.append(a[i-1][j-1]+a[i-1][j])
            t.append(1)
            a.append(t)
            print(t,i)
        return a