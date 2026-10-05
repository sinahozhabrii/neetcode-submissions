class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent = []
        for i in s:
            if i.isalnum():
                sent.append(i)
        new_sent = "".join(sent).lower()

        return new_sent == new_sent[::-1]
