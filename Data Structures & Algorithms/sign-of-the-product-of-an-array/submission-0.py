class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            if i<0:
                n+=1
            elif i==0:
                return 0
        return -1 if n%2 else 1