"""Wuff Wuff DOGString"""
# pylint: disable=disallowed-name
from typing import Callable


def _foo(bar: str) -> float:
    """no"""
    return float(bar)

def use_foo_factory(foo: Callable) -> Callable[[list[str]], list[float]]:
    """ja"""

    def _real_foo(bars: list[str]):
        return [foo(b) for b in bars]

    return _real_foo

use_foo = use_foo_factory(_foo)
