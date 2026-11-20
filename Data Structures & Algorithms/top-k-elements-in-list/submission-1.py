class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        return [key for key, v in sorted(mapping.items(), key=lambda i: i[1], reverse=True)][:k]