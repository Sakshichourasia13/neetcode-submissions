class MyLinkedList:

    def __init__(self):
        self.ll=[]
        self.lth=0

    def get(self, index: int) -> int:
        if index>=0 and index<self.lth:
            return self.ll[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.ll[::]=[val]+self.ll
        self.lth+=1

    def addAtTail(self, val: int) -> None:
        self.ll.append(val)
        self.lth+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.lth<index:
            return
        elif self.lth==index:
            self.ll.append(val)
            self.lth+=1
        else:
            self.ll[::]=self.ll[:index]+[val]+self.ll[index:]
            self.lth+=1


    def deleteAtIndex(self, index: int) -> None:
        if self.lth>index and index>=0:
            self.ll.pop(index)
            self.lth-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)