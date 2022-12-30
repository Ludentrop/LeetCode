class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = [i for i in nums if bool(i)]
        z = nums.count(0)
        nums.clear()
        nums += s + [0] * z
