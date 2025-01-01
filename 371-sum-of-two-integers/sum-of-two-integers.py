class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to limit the integers to 32 bits
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        while b != 0:
            # Carry is AND operation shifted left by 1
            carry = (a & b) & MASK
            # Sum without carry is XOR
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        # If a is negative in 32-bit representation, convert to Python's integer
        return a if a <= INT_MAX else ~(a ^ MASK)
