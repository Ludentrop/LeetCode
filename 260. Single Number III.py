from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [item[0] for item in Counter(nums).items() if item[1] == 1]
