class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dp=[None]*capacity
        self.size=0

    def get(self, i: int) -> int:
        return self.dp[i]

    def set(self, i: int, n: int) -> None:
        self.dp[i]=n

    def pushback(self, n: int) -> None:
        if self.size==len(self.dp):
            self.resize()

        self.dp[self.size]=n
        self.size+=1

    def popback(self) -> int:
        pp=self.dp[self.size-1]
        self.dp[self.size-1]=None
        self.size-=1
        return pp

    def resize(self) -> None:
        temp=[None]*len(self.dp)
        self.dp.extend(temp)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.dp)