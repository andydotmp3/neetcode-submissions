class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # products = [1] * len(nums)
        # for i, num in enumerate(nums):
        #     for j in range(len(products)):
        #         if i == j:
        #             continue
        #         if products[j] == 0:
        #             continue
        #         products[j] *= num
        # return products

        prefixes = [1] * (len(nums) + 1)
        suffixes = [1] * (len(nums) + 1)
        finals = [1] * len(nums)

        for i, num in enumerate(nums):
            prefixes[i + 1] = num * prefixes[i]
        for i, num in enumerate(reversed(nums)):
            suffixes[i + 1] = num * suffixes[i]

        suffixes.reverse()
        for i in range(len(nums)):
            finals[i] = prefixes[i] * suffixes[i + 1]
        return finals


        