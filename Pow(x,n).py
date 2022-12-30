class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (-100.0 < x < 100.0) and (-2**31 <= n <= 2**31-1) and (-10**4 <= pow(x, n) <= 10**4):
            return pow(x, n)
        return 0
