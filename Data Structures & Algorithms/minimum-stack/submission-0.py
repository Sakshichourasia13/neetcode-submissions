class MinStack:

    def __init__(self):
        self.st=[]

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        if self.st:
            return min(self.st)
