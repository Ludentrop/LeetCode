class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif 0 not in nums:
            nums.append(0)
        nums.sort()
        index = nums.index(0)

        try:
            if abs(nums[index-1]) < nums[index+1]:
                return nums[index-1]
            return nums[index+1]
        except IndexError:
            return nums[index-1]
