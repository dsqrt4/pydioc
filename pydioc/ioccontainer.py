from collections import namedtuple
from typing import TypeVar, Protocol, runtime_checkable, Any


class Error(Exception):
    pass


class AmbiguousRib(Error):
    def __init__(self, msg):
        self.message = f"ambiguous rib identifier {msg}"


T = TypeVar('T')


@runtime_checkable
class IocContainer(Protocol):
    def register_rib(self, obj: Any, name=None) -> None:  ...

    def get_rib_by_type(self, t: type(T)) -> list[T]: ...

    def get_rib_by_name(self, name: str) -> list[Any]: ...

    def get_rib_by_qualifier(self, qualifier: str) -> list[Any]: ...


Rib = namedtuple('Rib', 'obj name')


class GenOneIocContainer:

    def __init__(self):
        self._ribs: list[Rib] = []

    def register_rib(self, obj: Any, name=None):
        self._ribs.append(Rib(obj, name if name is not None else type(obj).__name__))

    def get_rib_by_type(self, t: type(T)) -> list[T]:
        return [rib.obj for rib
                in self._ribs
                if isinstance(rib.obj, t)]

    def get_rib_by_name(self, name: str) -> list[Any]:
        return [rib.obj for rib
                in self._ribs
                if rib.name == name]

    def get_rib_by_qualifier(self, qualifier: str) -> list[Any]:
        pass
