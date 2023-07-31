from typing import TypeVar, Protocol, Optional

T = TypeVar('T')


class IocContainer(Protocol):
    def register_rib(self, obj: any) -> None:  ...

    def get_rib(self, t: type(T)) -> Optional[T]: ...
