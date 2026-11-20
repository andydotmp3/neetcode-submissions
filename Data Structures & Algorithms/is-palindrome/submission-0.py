class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatted = [char.lower() for char in s if char.isalnum()]
        print(s_formatted)
        for i in range(len(s_formatted)):
            if s_formatted[i] != s_formatted[-i - 1]:
                return False

        
        return True