class LinkedList:
    
    def __init__(self):
        self.ll=[]

    def get(self, index: int) -> int:
        return self.ll[index] if index<len(self.ll) else -1

    def insertHead(self, val: int) -> None:
        self.ll=[val]+self.ll[::]

    def insertTail(self, val: int) -> None:
        self.ll.append(val)

    def remove(self, index: int) -> bool:
        if index<len(self.ll):
            self.ll.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        return self.ll
