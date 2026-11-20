class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, item in enumerate(nums):
            if target - item in mapping:
                return [mapping[target - item], i]
            mapping[item] = i