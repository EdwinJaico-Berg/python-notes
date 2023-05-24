"""Learning about collections.abc"""
from collections.abc import Iterable, Mapping, MutableMapping, Sequence
from typing import TypeVar

KT = TypeVar('KT')
VT = TypeVar('VT')

"""Type hinting 
Useful for the user as it allows for autocompletion.
What is often not considered is the difficulty that users might face. If 
their input is not a dict, then their editor might complain, although the
function may still be applicable."""


def delete_min_key(d: dict[int, str]) -> None:
    if not d:
        return
    key = min(d)
    del d[key]


def delete_min_key_two(d: MutableMapping) -> None:
    if not d:
        return
    key = min(d)
    del d[key]


"""
Runtime Interface Checking
"""


def deep_min(d):
    if isinstance(d, Mapping):
        return min(deep_min(v) for v in d.values())
    elif isinstance(d, Iterable):
        return min(deep_min(v) for v in d)
    else:
        return d


"""Defining your own mutable mapping"""


class InvertibleDict(MutableMapping[KT, VT]):
    """An invertible (one-to-one) mapping."""

    __slots__ = ('_forward', '_backward')

    _forward: dict[KT, VT]
    _backward: dict[VT, KT]

    def __init__(self,
                 forward: dict[KT, VT] | None = None,
                 /, *,
                 _backward: dict[VT, KT] | None = None
                 ):
        if forward is None: # empty init
            self._forward = {}
            self._backward = {}
        elif _backward is not None: # inverse init (private)
            self._forward = forward
            self._backward = _backward
        else:
            self._forward = forward
            self._backward = {value: key for key, value in self._forward.items()}
            self._check_non_invertible()

    def _check_non_invertible(self):


    def _raise_non_invertible(self, key1: KT, key2: KT, value: VT):...

    @property
    def inv(self) -> InvertibleDict[VT, KT]:
        """A mutable viewe of the inverse dict."""
        return self.__class__(self._backward, _backward=self._forward)

    def __getitem__(self, item: KT) -> VT:
        return self._forward[item]

    def __setitem__(self, key: KT, value: VT):
        missing = object()
        old_key = self._backward.get(value, missing)
        if old_key is not missing and old_key != key: # {1: "a"} -> {1: "a", 2: "a"}
            # value is already mapped to a different key
            self._raise_non_invertible(old_key, key, value)

        old_value = self._forward.get(key, missing) # {1: "a"}/{"a": 1} -> {1: "b"}/{"b": 1}
        if old_value is not missing:
            del self._backward[old_value]

        self._forward[key] = value
        self._backward[value] = key

    def __delitem__(self, key: KT):
        value = self._forward[key]
        del self._forward[key]
        del self._backward[value]

    def __iter__(self):
        return iter(self._forward)

    def __len__(self):
        return len(self._forward)

    def __repr__(self):...

    def clear(self) -> None:
        self._forward.clear()
        self._backward.clear()