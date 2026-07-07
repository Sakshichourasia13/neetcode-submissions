class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return 'NONE'
        enc=[]
        for i in strs:
            s=""
            for j in i:
                s+=chr(ord(j)+1)
            # print(s)
            enc.append(s)
        return " ".join(enc)
    def decode(self, s: str) -> List[str]:
        if s=='NONE':
            return []
        dec=[]
        st=""
        for i in s:
            if i==" ":
                dec.append(st)
                st=""
            else:
                st+=chr(ord(i)-1)
        dec.append(st)
        return dec
