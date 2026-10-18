class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                input += s[i].lower()
        return input == input[::-1]
        