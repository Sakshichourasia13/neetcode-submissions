class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num and num[-1] in '24680':
            num=num[:-1]
        return num if num else ""
