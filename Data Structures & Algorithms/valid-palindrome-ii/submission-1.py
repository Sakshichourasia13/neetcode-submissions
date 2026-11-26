class Solution:
    def validPalindrome(self, s: str) -> bool:
        a=s[1:]
        if s==s[::-1] or a==a[::-1]:
            return True
        for i in range(1,len(s)):
            a=s[:i]+s[i+1:]
            if a==a[::-1]:
                return True
        return False