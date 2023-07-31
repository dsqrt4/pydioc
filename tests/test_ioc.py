from collections import Iterable
from typing import Any

import pytest

from pydioc.ioccontainer import GenOneIocContainer, IocContainer


def test_GenOneIocContainer_is_instance_of_IocContainer():
    assert isinstance(GenOneIocContainer(), IocContainer)


class DescribeGetRibByType:
    class WhenTheContainerIsEmpty:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            return GenOneIocContainer()

        def it_returns_empty(self, ioc_container):
            assert [] == ioc_container.get_rib_by_type(str)

    class WhenThereAreRibsInIt:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            ioc_container = GenOneIocContainer()
            ioc_container.register_rib(42)
            ioc_container.register_rib('Hello, World!')
            return ioc_container

        def it_returns_empty_if_no_rib_of_such_type_was_registered(self, ioc_container):
            result = ioc_container.get_rib_by_type(list)
            assert [] == result

        @pytest.mark.parametrize('type_to_find, expected_ribs', [
            (int, [42]),
            (Iterable, ['Hello, World!']),
            (object, [42, 'Hello, World!'])
        ])
        def it_returns_the_right_object(self, ioc_container, type_to_find, expected_ribs):
            result = ioc_container.get_rib_by_type(type_to_find)
            assert expected_ribs == result


class DescribeGetRibByName:
    class WhenTheContainerIsEmpty:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            return GenOneIocContainer()

        def it_returns_empty(self, ioc_container):
            assert [] == ioc_container.get_rib_by_name('answer')

    class WhenThereAreRibsInIt:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            ioc_container = GenOneIocContainer()
            ioc_container.register_rib(42, name='answer')
            ioc_container.register_rib('Hello, World!')
            return ioc_container

        def it_returns_empty_if_no_rib_of_such_type_was_registered(self, ioc_container):
            result = ioc_container.get_rib_by_name(list)
            assert [] == result

        @pytest.mark.parametrize('name_to_find, expected_ribs', [
            ('answer', [42]),
            ('str', ['Hello, World!'])
        ])
        def it_returns_the_right_object(self, ioc_container, name_to_find, expected_ribs):
            result = ioc_container.get_rib_by_name(name_to_find)
            assert expected_ribs == result


class DescribeGetRibByQualifier:
    class WhenTheContainerIsEmpty:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            return GenOneIocContainer()

        def it_returns_empty(self, ioc_container):
            assert [] == ioc_container.get_rib_by_qualifier('answer')

    class WhenThereAreRibsInIt:
        @pytest.fixture
        def ioc_container(self) -> IocContainer:
            ioc_container = GenOneIocContainer()
            ioc_container.register_rib(42, name='answer')
            ioc_container.register_rib('Hello, World!')
            return ioc_container

        def it_returns_empty_if_no_rib_of_such_type_was_registered(self, ioc_container):
            result = ioc_container.get_rib_by_qualifier(list)
            assert [] == result

        @pytest.mark.parametrize('qualifier, expected', [
            ('answer', [42]),
            ('str', ['Hello, World!'])
        ])
        def it_returns_the_right_object(self, ioc_container, qualifier, expected):
            result = ioc_container.get_rib_by_qualifier(qualifier)
            assert expected == result
