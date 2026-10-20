class Solution:
    def __init__(self):
        pass
    def encode(self, longUrl: str) -> str:
        return ''.join(chr(ord(c)+1) for c in longUrl)
    def decode(self, shortUrl: str) -> str:
        return ''.join(chr(ord(c)-1) for c in shortUrl)
