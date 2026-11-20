class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            encoding += f"{len(string)}"
            encoding += "-"
        encoding += "."
        for string in strs:
            encoding += string
        return encoding

    def decode(self, s: str) -> List[str]:
        l = []
        # find the sizes first
        sizes_end_index = -1
        for i, char in enumerate(s):
            if char == ".": 
                sizes_end_index = i
                break

        sizes = s[:sizes_end_index].split('-')
        prev_index = sizes_end_index + 1
        for size in sizes[:-1]:
            size = int(size)
            l.append(s[prev_index:prev_index + size])
            prev_index = prev_index + size

        return l
            

