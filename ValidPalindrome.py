class Solution:
    def isPalindrome(self, s: str) -> bool:
        let = ''

        for i in s.lower():
            if i not in '@~`#$%^&*()\'{}[].""'',!?:;=+-_/\ ':  # fucking symbols!
                let += i

        return let == let[::-1]
        
