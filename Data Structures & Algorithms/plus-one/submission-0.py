class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        n=int(''.join(digits))+1
        a=[]
        for i in str(n):
            a.append(i)
        return a
