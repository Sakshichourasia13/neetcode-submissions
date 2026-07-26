class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        o=0
        mx=0

        for i in nums:
            if i==1:
                o+=1
            else:
                o=0
            mx=max(o,mx)
        return mx