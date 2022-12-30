class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == 1 or str(num ** 0.5).endswith('0')
        
