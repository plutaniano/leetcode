class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Is this cheating?"""
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary1(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        a = list(a.rjust(length, "0"))
        b = list(b.rjust(length, "0"))

        result = []
        carry = 0

        while a:
            n = [a.pop(), b.pop(), str(carry)].count("1")
            if n == 0:
                result.insert(0, "0")
                carry = 0
            elif n == 1:
                result.insert(0, "1")
                carry = 0
            elif n == 2:
                result.insert(0, "0")
                carry = 1
            else:
                result.insert(0, "1")
                carry = 1
        if carry:
            result.insert(0, "1")

        return "".join(result)
