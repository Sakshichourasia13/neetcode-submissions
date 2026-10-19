class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for i in s:
            if i in '1234567890':
                st.pop()
            else:
                st.append(i)
        return "".join(st)
