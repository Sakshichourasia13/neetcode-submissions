class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev=[]
        od=[]
        for i in nums:
            if i%2:
                od.append(i)
            else:
                ev.append(i)

        nums[::]=ev[::]+od[::]
        return nums