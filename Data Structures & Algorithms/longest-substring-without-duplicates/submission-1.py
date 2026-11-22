class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = {s[0]: 0}
        left = 0
        right = 1
        longest = 0
        # stop when right gets to the end of the string
        while right != len(s):

            # if we've seen this new character before
            if s[right] in seen:
                # compute longest
                longest = max(right - left, longest)

                # move left until the seen character is gone
                while s[right] in seen:
                    del seen[s[left]]
                    left += 1
                seen[s[right]] = right
                right += 1
            else:
                seen[s[right]] = right
                right += 1

        return max(longest, right - left)
