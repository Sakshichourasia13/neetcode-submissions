class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                z+=1
            else:
                i+=1
        nums[::]=nums[::]+[0]*z