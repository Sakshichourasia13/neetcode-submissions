class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st=set()
        for i in emails:
            n=i.index('@')
            s=i[:n]
            if '+' in s:
                p=i.index('+')
                s=s[:p]
            s=s.replace(".","")
            st.add(s+i[n:])

        return len(st)