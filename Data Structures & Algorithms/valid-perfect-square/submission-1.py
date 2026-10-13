from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num))*int(sqrt(num))==num