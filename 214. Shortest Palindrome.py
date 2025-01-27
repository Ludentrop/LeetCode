class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        def is_palindrome(s):
            return s == s[::-1]

        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return s[i:][::-1] + s

# very slow
