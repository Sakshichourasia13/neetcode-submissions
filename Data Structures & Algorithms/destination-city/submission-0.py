class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        has={i[0]:i[1] for i in p}

        s=p[0][0]
        while s in has:
            s=has[s]
        return s
