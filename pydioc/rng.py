from typing import runtime_checkable, Protocol


@runtime_checkable
class RNG(Protocol):
    def randInt(self) -> int: ...


class FakeRNG:
    def randInt(self) -> int:
        return 3