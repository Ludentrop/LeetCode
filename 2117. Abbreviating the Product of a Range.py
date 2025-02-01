from functools import reduce
import operator
import sys


sys.set_int_max_str_digits(0)

# TODO: solve without type transformation
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        prod = str(reduce(operator.mul, range(left, right+1), 1))
        zeros = 0

        while prod[::-1][zeros] == '0':
            zeros += 1

        if zeros:
            prod = prod[:-zeros]

        if len(prod) > 10:
            return f'{prod[:5]}...{prod[-5:]}e{zeros}'

        return f'{prod}e{zeros}'
