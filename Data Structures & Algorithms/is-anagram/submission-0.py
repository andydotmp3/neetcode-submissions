class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for letter in s:
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1
        for letter in t:
            if letter not in counts:
                return False
            counts[letter] -= 1

        for key, value in counts.items():
            if value != 0:
                return False
        return True