class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        if len(nums)<=2:
            return nums[0]
        has={}
        for i in nums:
            if i in has:
                has[i]+=1
                if has[i]>n:
                    return i
            else:
                has[i]=1
        