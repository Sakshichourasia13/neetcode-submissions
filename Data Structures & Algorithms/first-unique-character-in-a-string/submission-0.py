class Solution:
    def firstUniqChar(self, s: str) -> int:
        has=Counter(s)
        for i in range(len(s)):
            if has[s[i]]==1:
                return i
        return -1