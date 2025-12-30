# ./src/examples_random_numbers_stream.py

from .random_numbers_stream import RandomNumbersStream


def example_endless_stream():
    """
    Example 1:
    Endless stream of random numbers in range [10, 100].
    """
    print("Example 1: Endless random numbers [10, 100]")
    numbers = RandomNumbersStream(min_value=10, max_value=100)

    for i, num in enumerate(numbers):
        print(num)
        if i == 4:  # stop manually to avoid infinite loop
            break

    print("-" * 40)


def example_even_numbers():
    """
    Example 2:
    Endless stream of even random numbers.
    """
    print("Example 2: Endless even random numbers [10, 100]")
    numbers = RandomNumbersStream(min_value=10, max_value=100)
    numbers.set_filter(lambda n: n % 2 == 0)

    for i, num in enumerate(numbers):
        print(num)
        if i == 4:
            break

    print("-" * 40)


def example_limited_even_numbers():
    """
    Example 3:
    Limited stream of even random numbers.
    """
    print("Example 3: 10 even random numbers [10, 100]")
    numbers = RandomNumbersStream(min_value=10, max_value=100)
    numbers.set_filter(lambda n: n % 2 == 0)
    numbers.set_limit(10)

    for num in numbers:
        print(num)

    print("-" * 40)


def example_sport_lotto():
    """
    Example 4:
    Sport Lotto — unique random numbers.
    """
    print("Example 4: Sport Lotto (unique numbers)")
    numbers = RandomNumbersStream(min_value=1, max_value=49)
    numbers.set_distinct()
    numbers.set_limit(10)

    for num in numbers:
        print(num)

    print("-" * 40)


def process_examples():
    example_endless_stream()
    example_even_numbers()
    example_limited_even_numbers()
    example_sport_lotto()
