class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has={}

        for i in nums:
            has[i]=has.get(i,0)+1

        has=sorted(has,key=lambda x:has[x])

        return has[-k:]