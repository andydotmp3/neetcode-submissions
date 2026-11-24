class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # this is just a frequency mapping
        mapping = {i: [] for i in range(len(nums) + 1)}
        numCount = {}
        for num in nums:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] += 1
                mapping[numCount[num] - 1].remove(num)
            mapping[numCount[num]].append(num)
        array = []
        for i in range(len(nums), 0, -1):
            array.extend(mapping[i])
            if len(array) == k:
                return array
        return array
