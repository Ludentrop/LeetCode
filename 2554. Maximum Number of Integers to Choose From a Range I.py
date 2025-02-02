class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)

        allowed_int = [x for x in range(1, n + 1) if x not in banned_set]

        current_sum = 0
        count = 0

        for num in allowed_int:
            if current_sum + num <= maxSum:
                current_sum += num
                count += 1
            else:
                break

        return count
