class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        seen = {}
        for num in nums:
            seen[num] = 0

        nums = list(seen.keys())
        print(nums)
        maximum = 0
        for num in nums:
            if num - 1 in seen:
                continue
            count = 1
            i = num + 1
            while i in seen:
                i += 1
                count += 1
            if count > maximum:
                maximum = count

        
        return maximum