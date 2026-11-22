class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        preprocessing = {}
        for char in s1:
            if char in preprocessing:
                preprocessing[char] += 1
            else:
                preprocessing[char] = 1
        left = 0

        """
        go through each character 1 by 1
        if the character is not in preprocessing, move left forward until it gets to right
        - when moving left forward, add in the chars back to preprocessing if and only if they're there already
        if the character appears in preprocessing, subtract it
        if it goes negative, move left forward until you find the next edition of that character
        - same note as above
        if we ever get all 0s, return true

        """
        for right in range(len(s2)):
            if s2[right] not in preprocessing:
                while left != right:
                    if s2[left] in preprocessing:
                        preprocessing[s2[left]] += 1
                    left += 1
                continue
            preprocessing[s2[right]] -= 1
            if preprocessing[s2[right]] < 0:
                while preprocessing[s2[right]] < 0:
                    if s2[left] in preprocessing:
                        preprocessing[s2[left]] += 1
                    left += 1
            if sum(list(preprocessing.values())) == 0:
                return True
        return False