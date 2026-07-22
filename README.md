# Python Data Structures and Algorithms Practice

[![CI](https://github.com/Tumelo4/assessment3_practice_data_structures/actions/workflows/ci.yml/badge.svg)](https://github.com/Tumelo4/assessment3_practice_data_structures/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python\&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-pytest-0A9EDC?logo=pytest\&logoColor=white)

A practical Python project for strengthening data-structure, algorithm and problem-solving skills through small implementations and automated tests.

The repository currently contains solutions for **41 of 50 challenges**. The exercises progress from core list and dictionary operations to more advanced topics such as recursion, caching, dependency resolution, rate limiting, circuit breakers and iterable processing.

## Current Status

| Area                   | Status                     |
| ---------------------- | -------------------------- |
| Implemented challenges | 41 of 50                   |
| Test framework         | pytest                     |
| Coverage reporting     | pytest-cov                 |
| Static checks          | flake8                     |
| CI environments        | Python 3.10, 3.11 and 3.12 |

## What This Project Demonstrates

* Python collections: lists, dictionaries, sets and tuples
* Recursive traversal of nested data
* Sorting, grouping, deduplication and reconciliation
* Sliding-window and frequency-based algorithms
* Generators and iterable processing
* LRU caching and deterministic hashing
* Dependency resolution using topological sorting
* Token-bucket rate limiting
* Circuit-breaker state transitions
* Unit testing, linting and CI automation

## Project Structure

```text
assessment3_practice_data_structures/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pytest.ini
├── README.md
├── requirements.txt
├── solution.py
└── tests/
    └── test_ds_practical.py
```

## Getting Started

### Prerequisites

* Python 3.10 or newer
* `pip`

### Installation

```bash
git clone https://github.com/Tumelo4/assessment3_practice_data_structures.git
cd assessment3_practice_data_structures
python -m venv .venv
```

Activate the virtual environment.

**macOS or Linux**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```bash
pytest tests/test_ds_practical.py -v
```

Run a specific test:

```bash
pytest tests/test_ds_practical.py -k "test_unique_sorted"
```

Run tests with coverage:

```bash
pytest tests/test_ds_practical.py --cov=solution --cov-report=term-missing
```

Run the critical lint checks used by CI:

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Implemented Challenges

### Core Collections and Processing

* Unique sorted values
* List rotation
* Character frequency maps
* Ordered list intersection
* Recursive list flattening
* Dictionary inversion and merge-with-sum
* Grouping by first letter
* Multi-field sorting
* Category-based tax calculation
* Anagram checking

### Nested Data and Algorithms

* Stable deduplication
* Windowed averages
* Recursive dictionary merging
* Normalised character frequencies
* Cartesian products
* Deep-key search
* Nested flattening
* Schema validation
* Record deduplication
* Deep dictionary differences
* Dot-path value lookup
* Grouping by multiple keys
* Sliding-window maximums
* Circular iterators
* Deep freezing of nested structures
* Record reconciliation
* Sensitive-data masking
* Fault-tolerant processing pipelines

### Systems-Oriented Exercises

* LRU cache
* Top-k frequency calculation
* JSON-style patch operations
* Deterministic hashing
* Dependency resolution
* Token-bucket rate limiter
* Circuit breaker
* Event debouncing
* Schema migration
* Iterable record joining

## Remaining Challenges

The following exercises are still planned:

* [ ] Chunk a list into fixed-size groups
* [ ] Sort even values before odd values
* [ ] Return the top-N dictionary entries
* [ ] Filter dictionary entries by value
* [ ] Safely read deeply nested values
* [ ] Transpose a matrix
* [ ] Bulk-update nested records
* [ ] Calculate the difference between two lists
* [ ] Recursively remove `None` values

## Continuous Integration

GitHub Actions runs on pushes and pull requests targeting `main`. The workflow:

1. Tests the project on Python 3.10, 3.11 and 3.12.
2. Checks for syntax errors and undefined names with flake8.
3. Runs the pytest suite with coverage.
4. Uploads the coverage report from the Python 3.12 job.

## Roadmap

* Complete the remaining nine challenges
* Improve edge-case coverage
* Refactor selected implementations for clearer complexity guarantees
* Add type hints and docstrings
* Separate challenge descriptions from implementations
* Add complexity notes for each solution

## Author

**Tumelo Mosomane**

* GitHub: [Tumelo4](https://github.com/Tumelo4)
