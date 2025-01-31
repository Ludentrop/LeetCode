class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        maximal = max(nums)
        if nums == list(range(1, maximal+1)) + [maximal]:
            return True
        return False
