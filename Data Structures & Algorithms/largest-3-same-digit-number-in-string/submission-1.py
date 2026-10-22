class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        mx=-1
        ans=""
        for i in range(len(nums)-2):
            n=nums[i:i+3]
            if len(set(n))==1:
                if mx<int(n):
                    ans=n
                    mx=int(n)
        return ans 