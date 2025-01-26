class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        mid_x = x / 2
        epsilon = .999
        for i in range(1000):
            next_x = (mid_x + x / mid_x) / 2
            if abs(next_x - mid_x) < epsilon:
                return int(next_x)
            mid_x = next_x
