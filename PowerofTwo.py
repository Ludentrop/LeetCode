class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if -2**31 <= n <= 2**31 - 1:
            for i in range(1, 32):
                if 2 == n ** (1/i) or n == 1:
                    return True
            return False
        return 0
