# HW28: Random Numbers Stream

## Task Definition

The goal of this homework is to implement a class `RandomNumbersStream` that allows generating and streaming random integers with advanced features such as **filtering**, **limiting**, and **distinct number generation**. The class must provide a flexible interface for producing random sequences according to user-defined rules.

### Required Methods

1. `__init__(self, min_value: int = -10**20, max_value: int = 10**20)`  
   Initializes the random number stream to generate numbers in the interval `[min_value, max_value]`. By default, the stream can produce an endless sequence.

2. `set_filter(self, predicate: Callable[[int], bool])`  
   Sets a filter function that determines which numbers should be yielded. Only numbers satisfying the predicate will be included in the stream.

3. `set_limit(self, limit: int)`  
   Limits the number of random numbers generated. After reaching this limit, iteration stops automatically.

4. `set_distinct(self)`  
   Enables a mode where only **unique numbers** are generated. Duplicate values will be skipped.

5. `reset_distinct(self)`  
   Disables the distinct mode, allowing repeated numbers to appear in the stream.

6. `__iter__(self) -> Iterator[int]`  
   Returns an iterator over the random numbers stream, respecting all configured filters, limits, and distinct settings.

---

## 📝 Description

`RandomNumbersStream` is designed for a variety of use cases where controlled random number generation is required:

-   Endless random numbers for simulation or testing
-   Streaming numbers with custom constraints
-   Generating non-repeating sequences for lottery or games
-   Efficiently handling very large ranges without excessive memory usage

The class is built to be flexible and memory-efficient. By combining **filtering**, **distinct value control**, and **iteration limits**, it can handle diverse scenarios while remaining performant even with extremely large ranges, e.g., from `-10**20` to `10**20`.

---

## 🎯 Purpose

The purpose of this project is to:

-   Demonstrate the design of a **custom iterable class** in Python
-   Explore **random number generation** with advanced constraints
-   Learn to combine **filtering**, **distinct values**, and **limiting** in a streaming context
-   Develop a memory-efficient solution that supports **endless iteration**
-   Provide practical examples for testing, simulation, and small-scale games

---

## 🔍 How It Works

### 1. Initialization

Upon creating a `RandomNumbersStream`, the minimum and maximum bounds are defined:

```python
numbers = RandomNumbersStream(min_value=1, max_value=100)
```

No numbers are generated until iteration begins.

### 2. Filtering

Filters allow only specific numbers to pass through:

```python
numbers.set_filter(lambda n: n % 2 == 0)  # only even numbers
```

During iteration, the generator checks each random number against the predicate.

### 3. Limiting

You can limit the number of values produced:

```python
numbers.set_limit(10)  # yield only 10 numbers
```

The generator stops automatically when the limit is reached.

### 4. Distinct Numbers

To generate unique numbers:

```python
numbers.set_distinct()
```

All repeated values are skipped. You can reset this behavior:

```python
numbers.reset_distinct()
```

### 5. Iteration

Iteration applies all configured settings:

```python
for num in numbers:
    print(num)
```

-   The generator yields numbers until the limit is reached
-   Filters are applied on-the-fly
-   Distinctness is enforced if enabled

---

## 📜 Output Example

### Endless Random Numbers

```python
numbers = RandomNumbersStream(min_value=1, max_value=10)
for i, num in enumerate(numbers):
    print(num)
    if i >= 4:  # stop manually
        break
```

### Limited Even Numbers

```python
numbers = RandomNumbersStream(min_value=1, max_value=10)
numbers.set_filter(lambda n: n % 2 == 0)
numbers.set_limit(5)

for num in numbers:
    print(num)
```

### Sport Lotto (Unique Numbers)

```python
numbers = RandomNumbersStream(min_value=1, max_value=49)
numbers.set_distinct()
numbers.set_limit(6)

for num in numbers:
    print(num)  # prints 6 unique numbers
```

---

## 📦 Usage

```python
from src.random_numbers_stream import RandomNumbersStream

numbers = RandomNumbersStream(min_value=1, max_value=100)
numbers.set_filter(lambda n: n % 5 == 0)
numbers.set_limit(10)
numbers.set_distinct()

for num in numbers:
    print(num)
```

---

## 🧪 Running Tests

Unit tests are provided in the `/tests` folder. To run the tests:

```bash
python -m unittest discover tests -v
```

Tests cover:

-   Endless number generation
-   Filtered sequences
-   Limited sequences
-   Distinct number generation
-   Combined scenarios (filter + limit + distinct)

---

## ✅ Dependencies

-   Python 3.10+
-   Standard library only (uses `random` and `typing` modules)

No external packages are required.

---

## 🗂 Project Structure

```
.
├── .gitignore
├── main.py
├── README.md
├── src
│   ├── __init__.py
│   ├── random_numbers_stream.py
│   └── examples_random_numbers_stream.py
└── tests
    └── test_random_numbers_stream.py
```

---

## 📊 Project Status

**Status:** Completed ✅

-   Supports endless and limited streams
-   Supports filtering and distinct value generation
-   Efficient for very large number ranges
-   Fully tested and documented

---

## 📄 License

MIT License

---

## 🧮 Conclusion

`RandomNumbersStream` is a flexible and memory-efficient tool for generating random numbers in Python.  
It can be used for:

-   Simulations
-   Testing applications
-   Games or lotteries
-   Any scenario requiring controlled random streams

By combining **filters**, **limits**, and **distinct value control**, it provides a versatile and reliable solution.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓  
© 2025 All rights reserved.
