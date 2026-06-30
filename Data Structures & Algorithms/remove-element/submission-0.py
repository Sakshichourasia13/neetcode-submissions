class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=[i for i in nums if i!=val]
        nums[::]=n[::]
        return len(n)