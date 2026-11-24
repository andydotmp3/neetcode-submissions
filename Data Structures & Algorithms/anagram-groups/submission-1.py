class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count not in mapping:
                mapping[count] = [string]
            else:
                mapping[count].append(string)
        return list(mapping.values())