class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 3:
            return n - 1
        if n % 2:
            if (n - 1) % 4:
                return 1 + self.integerReplacement(n + 1)
            return 1 + self.integerReplacement(n - 1)
        return 1 + self.integerReplacement(n // 2)
