from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        has={}
        ans=0
        print(has)
        for i in s:
            has[i]=has.get(i,0)+1
            if has[i]%2==0:
                ans+=2
        for i in has:
            if has[i]%2:
                ans+=1
                break
        return ans
        
