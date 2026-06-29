class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        st=[]
        for i in range(len(arr)-1,-1,-1):
            if not st:
                st.append(arr[i])
                arr[i]=-1
            elif st[-1]<arr[i]:
                st.append(arr[i])
                arr[i]=st[-2]
            else:
                arr[i]=st[-1]
        return arr