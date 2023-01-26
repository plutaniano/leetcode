class MyQueue:
    def __init__(self):
        self.inbound = []
        self.outbound = []

    def push(self, x: int) -> None:
        self.inbound.append(x)

    def move(self) -> None:
        if not self.outbound:
            while self.inbound:
                value = self.inbound.pop()
                self.outbound.append(value)

    def pop(self) -> int:
        self.move()
        return self.outbound.pop()

    def peek(self) -> int:
        self.move()
        return self.outbound[-1]

    def empty(self) -> bool:
        return not (self.inbound or self.outbound)
