class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        if nums.count(0)>1:
            return [0]*len(nums)
            
        for i in nums:
            if i!=0:
                pro*=i
            
        ans=[0]*len(nums)

        if 0 in nums:
            ans[nums.index(0)]=pro
            return ans


        for i in range(len(nums)):
            if nums[i]!=0:
                ans[i]=pro//nums[i]
        return ans
