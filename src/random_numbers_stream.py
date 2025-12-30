# ./src/random_numbers_stream.py

from random import randint
from typing import Callable, Iterator, Optional, Set


class RandomNumbersStream:
    """
    Endless (or limited) stream of random integers with optional filtering.

    Supports:
    - value range [min_value, max_value]
    - optional predicate filter
    - optional generation limit
    - optional distinct values mode
    """

    def __init__(self, min_value: int, max_value: int) -> None:
        """
        Initialize random number stream.

        Args:
            min_value: Minimum generated value (inclusive).
            max_value: Maximum generated value (inclusive).
        """
        self._min: int = min_value
        self._max: int = max_value
        self._filter: Optional[Callable[[int], bool]] = None
        self._limit: Optional[int] = None
        self._distinct: bool = False
        self._generated: Set[int] = set()

    def set_filter(self, predicate: Callable[[int], bool]) -> None:
        """
        Set a filter predicate for generated numbers.

        Args:
            predicate: Function that returns True for allowed numbers.
        """
        self._filter = predicate

    def set_limit(self, limit: int) -> None:
        """
        Set maximum amount of numbers to generate.

        Args:
            limit: Maximum number of yielded values.
        """
        self._limit = limit

    def set_distinct(self) -> None:
        """
        Enable distinct values mode.
        """
        self._distinct = True
        self._generated.clear()

    def reset_distinct(self) -> None:
        """
        Disable distinct values mode.
        """
        self._distinct = False
        self._generated.clear()

    def __iter__(self) -> Iterator[int]:
        """
        Generate random numbers according to configured rules.

        Yields:
            Random integers matching filter, limit and distinct settings.
        """
        count = 0

        while True:
            if self._limit is not None and count >= self._limit:
                break

            num = randint(self._min, self._max)

            if self._filter is not None and not self._filter(num):
                continue

            if self._distinct and num in self._generated:
                continue

            if self._distinct:
                self._generated.add(num)

            yield num
            count += 1
