class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        i=0
        if n==0:
            return True
        if len(fb)==1:
            return fb[0]==0 and n==1
                
        
        while n>0 and i<len(fb):
            if i==0 and fb[1]==fb[0]==0:
                fb[0]=1
                n-=1
            elif i+1<len(fb) and fb[i-1]==fb[i]==fb[i+1]==0:
                fb[i]=1
                n-=1
            elif i+1==len(fb) and fb[i-1]==fb[i]==0:
                fb[i]=1
                n-=1
            i+=1
        return not n