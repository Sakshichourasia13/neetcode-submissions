class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            g=0
            for i in str(n):
                g+=(int(i)**2)
            n=g
        
        return True
