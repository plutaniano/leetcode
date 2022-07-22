class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        values = []
        for t in tokens:
            try:
                value = int(t)
            except ValueError:
                a, b = values.pop(), values.pop()
                match t:
                    case "*":
                        value = a * b
                    case "+":
                        value = a + b
                    case "-":
                        value = b - a
                    case "/":
                        value = int(b / a)
            finally:
                values.append(value)
        return values[0]
