class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        
        mask = 0xffffffff

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
