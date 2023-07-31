import itertools
from typing import TypeVar, runtime_checkable, Generic, Optional, Sequence

T = TypeVar('T')


@runtime_checkable
class Repository(Generic[T]):
    def find_by_id(self, id: int) -> Optional[T]: ...

    def find_all(self) -> Sequence[T]: ...


class NumberRepository:
    def find_by_id(self, id: int) -> Optional[str]:
        return f"#{id}"

    def find_all(self) -> Sequence[str]:
        for i in range(0, 100):
            yield f"#{i}"
