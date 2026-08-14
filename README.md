# Simple Python Projects

A collection of small Python projects created to practice **programming fundamentals, object-oriented programming, algorithms, testing, user input, and Turtle graphics**.

Each project focuses on a different area of Python development and demonstrates practical use of core programming concepts.

---

## Projects

### 1. Turtle Table & Cake Drawing

**File:**

```text
Creating table.py
```

An interactive Turtle graphics program that generates a table and a decorated multi-layer cake based on user input.

### Features

* User-defined table dimensions
* User-selected colors
* Input validation
* Table-top drawing
* Table-leg drawing
* Multi-layer cake generation
* Candle decorations
* Star decorations
* Turtle fill colors
* Modular drawing functions
* Interactive user input

### User Inputs

The program asks the user to provide:

* Table length
* Table width
* Table color
* Cake length
* Cake width

### Running the Project

```bash
python "Creating table.py"
```

A Turtle graphics window will open and display the generated drawing.

---

## 2. Polygon Class

**Directory:**

```text
Polygon class/
```

An object-oriented Python project centered around a reusable `Polygon` class.

The project focuses on encapsulation, validation, comparison, and automated testing.

### Features

* Polygon name storage
* Side length storage
* Getter methods
* Setter methods
* Side length validation
* Equality comparison
* Inequality comparison
* String representation
* Circumference calculation
* Automated testing with `pytest`

### Example

```python
from polygon import Polygon

triangle = Polygon("Triangle", [3, 4, 5])

print(triangle.calculate_circumference())
```

Output:

```text
12
```

### Validation

Polygon side lengths must be positive.

For example:

```python
Polygon("Triangle", [3, 0, 5])
```

raises a `ValueError` because one of the side lengths is zero.

### Running the Tests

Navigate to the project directory:

```bash
cd "Polygon class"
```

Then run:

```bash
pytest
```

or:

```bash
python -m pytest
```

---

## 3. Sorting & Searching

**Directory:**

```text
sorting search/
```

A Python algorithms project that implements and compares common sorting and searching techniques.

### Implemented Sorting Algorithms

* Insertion Sort
* Merge Sort

### Implemented Searching Algorithms

* Linear Search
* Binary Search

### Program Flow

The sorting and searching program:

1. Generates random integer data
2. Sorts data using insertion sort
3. Performs binary search operations
4. Generates another dataset
5. Sorts it using merge sort
6. Performs linear searches
7. Performs binary searches
8. Measures search execution time
9. Compares algorithm behavior

---

## Algorithm Complexity

| Algorithm      | Time Complexity |
| -------------- | --------------- |
| Insertion Sort | O(n²)           |
| Merge Sort     | O(n log n)      |
| Linear Search  | O(n)            |
| Binary Search  | O(log n)        |

Binary search requires sorted data before it can work correctly.

Linear search can operate on unsorted data.

---

## Custom Array Implementation

The project includes:

```text
arrays.py
```

which provides a fixed-length array abstraction used by the sorting and searching project.

This helps demonstrate lower-level data structure concepts instead of relying only on Python's built-in list type.

---

## Running the Sorting & Searching Project

Navigate to:

```bash
cd "sorting search"
```

Then run:

```bash
python sorting_search_demo.py
```

The program will request an array size before generating and processing the data.

---

## Technologies Used

* Python 3
* Python Standard Library
* Turtle
* `array`
* `random`
* `time`
* `pytest`

---

## Repository Structure

```text
Simple-Python-Projects/
│
├── Creating table.py
│
├── Polygon class/
│   ├── polygon.py
│   └── test_polygon.py
│
├── sorting search/
│   ├── arrays.py
│   └── sorting_search_demo.py
│
└── README.md
```

---

## Setup

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd Simple-Python-Projects
```

Most projects use only Python's standard library.

For the Polygon tests, install `pytest`:

```bash
python -m pip install pytest
```

---

## Skills Demonstrated

This repository demonstrates experience with:

* Python syntax
* Variables and data types
* Conditionals
* Loops
* Functions
* Modular programming
* User input
* Input validation
* Object-oriented programming
* Encapsulation
* Special methods
* Exception handling
* Unit testing
* Data structures
* Sorting algorithms
* Searching algorithms
* Recursion
* Algorithmic complexity
* Performance measurement
* Turtle graphics

---

## Project Scope

These projects were created as educational programming exercises.

The repository is intended to demonstrate learning and practical experience across multiple Python concepts rather than represent a single production application.

---

## Status

**Completed Educational Python Project Collection**
