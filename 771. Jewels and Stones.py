class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for jewel in jewels:
            counter += stones.count(jewel)

        return counter
