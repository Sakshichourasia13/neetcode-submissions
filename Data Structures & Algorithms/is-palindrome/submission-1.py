class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=[i for i in s if i.isalnum()]
        return a==a[::-1]