# It is a slow shitcode!

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            inbase = ''.join(self.up2down(n, base))
            if inbase != inbase[::-1]:
                return False
        return True


    def up2down(self, n: int, base: int) -> list:
        result = []
        while n:
            result.append(str(n % base))
            n //= base

        return result[::-1]
