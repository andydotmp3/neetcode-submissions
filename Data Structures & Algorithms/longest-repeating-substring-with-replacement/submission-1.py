class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            # add to seen
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1

            if len(seen) == 1:
                continue
            

            # too many characters
            """
            if we've only encountered one kind of character, great
            if not, we need some way of eliminating the "most encountered" one so far
            then tallying up however many other ones there have been
            if that exceeds k, we gotta delete until one of those two conditions is no longer met
            """

            values = list(seen.values())
            if sum(values) - max(values) > k:
                longest = max(longest, right - left)
                while sum(values) - max(values) > k:
                    seen[s[left]] -= 1
                    left += 1
                    values = list(seen.values())
        return max(longest, right - left + 1)