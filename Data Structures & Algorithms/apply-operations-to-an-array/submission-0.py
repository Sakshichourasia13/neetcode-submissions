class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i+1<len(nums):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        i=0
        c=nums.count(0)
        nums=[i for i in nums if i!=0]
        nums.extend([0]*c)
        return nums
        
