class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search from 1-max and check how many hours it will take to eat at that rate
        """

        left = 1
        right = max(piles)

        last_working_k = -1
        while left <= right:
            k = (left + right) // 2
            # can koko finish all bananas if he eats at this rate?
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            # print(f"{k=}, {hours=}")
            if hours > h:
                left = k + 1
            elif hours <= h:
                right = k - 1
                last_working_k = k
        return last_working_k