class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        inc,dec=1,1
        mx=0
        c,d=False,False

        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                inc+=1
                c,d=True,False
            elif nums[i-1]>nums[i]:
                dec+=1
                c,d=False,True
            else:
                c=d=False
            mx=max(mx,max(inc,dec))
            if not d:
                dec=1
            if not c:
                inc=1
        return mx

