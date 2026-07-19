class MyHashMap:

    def __init__(self):
        self.has={}

    def put(self, key: int, value: int) -> None:
        self.has[key]=value

    def get(self, key: int) -> int:
        return self.has[key] if key in self.has else -1
        

    def remove(self, key: int) -> None:
        if key in self.has:
            del self.has[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)