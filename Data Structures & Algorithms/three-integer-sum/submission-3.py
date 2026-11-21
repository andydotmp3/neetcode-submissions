class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        found = []
        print(f"{nums=}")
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                continue
            twoSums = self.twoSumModified(nums[i + 1:], -num)
            for pair in twoSums:
                found.append([num, pair[0], pair[1]])
            seen[num] = True

        return found

    def twoSumModified(self, nums: List[int], target: int) -> List[List[int]]:
        seen = {}
        pairs = []
        pair_made_with = {}
        for i in range(len(nums)):
            if nums[i] in pair_made_with:
                continue
            if target - nums[i] in seen:
                pairs.append([target - nums[i], nums[i]])
                pair_made_with[nums[i]] = True
            seen[nums[i]] = i
        return pairs