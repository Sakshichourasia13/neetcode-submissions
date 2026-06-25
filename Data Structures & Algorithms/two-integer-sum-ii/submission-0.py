class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        has={}

        for i in range(len(arr)):
            if arr[i] in has:
                return [has[arr[i]],i+1]
            has[target-arr[i]]=i+1
        return []