import numpy as np


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for raw, col in zip(matrix, np.transpose(matrix)):
            if not (set(raw) == set(col) == set(range(1, len(matrix)+1))):
                return False
        return True
