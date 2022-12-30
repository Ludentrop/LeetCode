import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.findall(rf"{p}", s)+[' ']

        if result[0] == s:
            return True
        return False
