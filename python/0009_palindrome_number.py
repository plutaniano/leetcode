class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        new = 0
        while x > new:
            new = new * 10 + x % 10
            x = x // 10
        return x == new or x == new // 10
