class Solution:
    def isPalindrome(self, num: int) -> bool:
        if -2 ** 32 <= num <= 2 ** 32 - 1:

            return str(num) == str(num)[::-1]

        return 0
