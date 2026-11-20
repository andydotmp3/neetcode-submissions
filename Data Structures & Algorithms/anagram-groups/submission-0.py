class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        overall_mapping = {}
        for string in strs:
            string_sorted = "".join(sorted(string))
            if string_sorted not in overall_mapping:
                overall_mapping[string_sorted] = [string]
            else:
                overall_mapping[string_sorted].append(string)
        return list(overall_mapping.values())