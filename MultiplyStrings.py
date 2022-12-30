class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1.strip('""'))
        num2 = int(num2.strip('""'))

        res = str(num1 * num2)
        
        return res
