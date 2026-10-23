# Test Design Document - Member A (Muhammad Arslan)

This document contains Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA) test designs for the assigned functions in `portion`.

---

## 1. Module `interval`

### 1.1 Function `closed(lower, upper)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-CL-01 | lower < upper | Valid (finite range) | lower=1, upper=5 | `[1, 5]` |
| ECP-CL-02 | lower == upper | Valid (singleton) | lower=3, upper=3 | `[3, 3]` |
| ECP-CL-03 | lower > upper | Valid (empty range) | lower=5, upper=1 | `()` |
| ECP-CL-04 | lower = -inf, finite upper | Valid (half-unbounded) | lower=-inf, upper=0 | `(-inf, 0]` |
| ECP-CL-05 | finite lower, upper = +inf | Valid (half-unbounded) | lower=0, upper=inf | `[0, +inf)` |
| ECP-CL-06 | lower = -inf, upper = +inf | Valid (fully unbounded) | lower=-inf, upper=inf | `(-inf, +inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-CL-01 | Degenerate interval (lower == upper) | lower=2, upper=2 | `[2, 2]` |
| BVA-CL-02 | Inverted order boundary (lower == upper + 1) | lower=3, upper=2 | `()` |
| BVA-CL-03 | Infinite lower bound (-inf is open) | lower=-inf, upper=5 | `(-inf, 5]` |
| BVA-CL-04 | Infinite upper bound (+inf is open) | lower=-5, upper=inf | `[-5, +inf)` |
| BVA-CL-05 | Negative to positive transition | lower=-1, upper=1 | `[-1, 1]` |

---

### 1.2 Function `open(lower, upper)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-OP-01 | lower < upper | Valid (finite range) | lower=1, upper=5 | `(1, 5)` |
| ECP-OP-02 | lower == upper | Valid (empty range) | lower=3, upper=3 | `()` |
| ECP-OP-03 | lower > upper | Valid (empty range) | lower=5, upper=1 | `()` |
| ECP-OP-04 | lower = -inf, finite upper | Valid (half-unbounded) | lower=-inf, upper=2 | `(-inf, 2)` |
| ECP-OP-05 | finite lower, upper = +inf | Valid (half-unbounded) | lower=2, upper=inf | `(2, +inf)` |
| ECP-OP-06 | lower = -inf, upper = +inf | Valid (fully unbounded) | lower=-inf, upper=inf | `(-inf, +inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-OP-01 | lower == upper boundary | lower=4, upper=4 | `()` |
| BVA-OP-02 | Adjacent integers | lower=1, upper=2 | `(1, 2)` |
| BVA-OP-03 | Float boundary delta | lower=1.0, upper=1.0001 | `(1.0, 1.0001)` |
| BVA-OP-04 | Negative boundary crossing zero | lower=-2, upper=0 | `(-2, 0)` |
| BVA-OP-05 | Infinite bounds | lower=-inf, upper=inf | `(-inf, +inf)` |

---

### 1.3 Function `openclosed(lower, upper)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-OC-01 | lower < upper | Valid (standard) | lower=1, upper=5 | `(1, 5]` |
| ECP-OC-02 | lower == upper | Valid (empty) | lower=2, upper=2 | `()` |
| ECP-OC-03 | lower > upper | Valid (empty) | lower=4, upper=1 | `()` |
| ECP-OC-04 | lower = -inf, finite upper | Valid (half-unbounded) | lower=-inf, upper=3 | `(-inf, 3]` |
| ECP-OC-05 | finite lower, upper = +inf | Valid (half-unbounded) | lower=1, upper=inf | `(1, +inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-OC-01 | Zero length boundary | lower=0, upper=0 | `()` |
| BVA-OC-02 | Minimal non-empty integer range | lower=0, upper=1 | `(0, 1]` |
| BVA-OC-03 | Negative boundary values | lower=-5, upper=-1 | `(-5, -1]` |
| BVA-OC-04 | Upper bound is +inf (forces open right) | lower=2, upper=inf | `(2, +inf)` |
| BVA-OC-05 | Inverted delta boundary | lower=1.0001, upper=1.0 | `()` |

---

### 1.4 Function `closedopen(lower, upper)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-CO-01 | lower < upper | Valid (standard) | lower=1, upper=5 | `[1, 5)` |
| ECP-CO-02 | lower == upper | Valid (empty) | lower=2, upper=2 | `()` |
| ECP-CO-03 | lower > upper | Valid (empty) | lower=6, upper=2 | `()` |
| ECP-CO-04 | lower = -inf, finite upper | Valid (half-unbounded) | lower=-inf, upper=4 | `(-inf, 4)` |
| ECP-CO-05 | finite lower, upper = +inf | Valid (half-unbounded) | lower=0, upper=inf | `[0, +inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-CO-01 | Degenerate boundary | lower=7, upper=7 | `()` |
| BVA-CO-02 | Minimal integer span | lower=3, upper=4 | `[3, 4)` |
| BVA-CO-03 | Lower bound is -inf (forces open left) | lower=-inf, upper=1 | `(-inf, 1)` |
| BVA-CO-04 | Upper bound is +inf | lower=-2, upper=inf | `[-2, +inf)` |
| BVA-CO-05 | Symmetric around zero | lower=-1, upper=1 | `[-1, 1)` |

---

### 1.5 Function `singleton(value)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-SG-01 | Positive integer | Valid | value=5 | `[5, 5]` |
| ECP-SG-02 | Negative integer | Valid | value=-10 | `[-10, -10]` |
| ECP-SG-03 | Zero | Valid | value=0 | `[0, 0]` |
| ECP-SG-04 | Float value | Valid | value=2.718 | `[2.718, 2.718]` |
| ECP-SG-05 | Infinite value | Valid (empty due to inf openness) | value=inf | `()` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-SG-01 | Value zero boundary | value=0 | `[0, 0]` |
| BVA-SG-02 | Negative infinity boundary | value=-inf | `()` |
| BVA-SG-03 | Positive infinity boundary | value=inf | `()` |
| BVA-SG-04 | Small float delta around zero | value=1e-9 | `[1e-9, 1e-9]` |
| BVA-SG-05 | Very large finite number | value=1e18 | `[1e18, 1e18]` |

---

### 1.6 Function `empty()`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Values | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-EM-01 | Default invocation | Valid | empty() | `()` |
| ECP-EM-02 | Property .empty | Valid | empty().empty | `True` |
| ECP-EM-03 | Property .atomic | Valid | empty().atomic | `True` |
| ECP-EM-04 | Length check | Valid | len(empty()) | `0` |
| ECP-EM-05 | Bounds of empty | Valid | (empty().lower, empty().upper) | `(inf, -inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Values | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-EM-01 | Boundary between empty and singleton | empty() vs singleton(0) | `len == 0` vs `len == 1` |
| BVA-EM-02 | Inversion boundary (lower > upper) | lower=inf, upper=-inf | `lower > upper` |
| BVA-EM-03 | Open boundary default | empty().left, empty().right | `(Bound.OPEN, Bound.OPEN)` |
| BVA-EM-04 | Intersection with any interval | empty() & [1, 2] | `()` |
| BVA-EM-05 | Union with any interval | empty() \| [1, 2] | `[1, 2]` |

---

### 1.7 Method `Interval.replace(left, lower, upper, right)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target & Arguments | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-RP-01 | Replace lower bound | Valid | `[1, 5].replace(lower=2)` | `[2, 5]` |
| ECP-RP-02 | Replace upper bound | Valid | `[1, 5].replace(upper=8)` | `[1, 8]` |
| ECP-RP-03 | Replace left openness | Valid | `[1, 5].replace(left=Bound.OPEN)` | `(1, 5]` |
| ECP-RP-04 | Replace right openness | Valid | `[1, 5].replace(right=Bound.OPEN)` | `[1, 5)` |
| ECP-RP-05 | Replace with callable | Valid | `[1, 5].replace(lower=lambda x: x + 2)` | `[3, 5]` |
| ECP-RP-06 | Non-atomic interval replacement | Valid | `([1, 2] \| [4, 5]).replace(lower=0)` | `[0, 2] \| [4, 5]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target & Arguments | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-RP-01 | Replace bound causing empty interval | `[1, 5].replace(lower=10)` | `()` |
| BVA-RP-02 | Replace bound to equal other bound with open side | `[1, 5].replace(lower=5, left=Bound.OPEN)` | `()` |
| BVA-RP-03 | Replace bound to equal other bound with closed sides | `[1, 5].replace(lower=5)` | `[5, 5]` |
| BVA-RP-04 | Callable ignoring infinity by default | `(-inf, 5].replace(lower=lambda x: x + 1)` | `(-inf, 5]` |
| BVA-RP-05 | Replace on already empty interval | `empty().replace(lower=1, upper=2)` | `[1, 2]` |

---

## 2. Module `ops`

### 2.1 Method `Interval.intersection(other)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-IN-01 | Overlapping closed intervals | Valid | a=`[1, 5]`, b=`[3, 8]` | `[3, 5]` |
| ECP-IN-02 | Disjoint intervals | Valid | a=`[1, 3]`, b=`[5, 8]` | `()` |
| ECP-IN-03 | Subset / contained interval | Valid | a=`[1, 10]`, b=`[3, 7]` | `[3, 7]` |
| ECP-IN-04 | Intersection with empty | Valid | a=`[1, 5]`, b=`()` | `()` |
| ECP-IN-05 | Intersection with self | Valid | a=`[1, 5]`, b=`[1, 5]` | `[1, 5]` |
| ECP-IN-06 | Non-atomic disjunction intersection | Valid | a=`[1, 3] \| [6, 9]`, b=`[2, 7]` | `[2, 3] \| [6, 7]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-IN-01 | Touching at closed endpoint | a=`[1, 4]`, b=`[4, 8]` | `[4, 4]` |
| BVA-IN-02 | Touching at open endpoint | a=`[1, 4)`, b=`[4, 8]` | `()` |
| BVA-IN-03 | Touching with both open | a=`[1, 4)`, b=`(4, 8]` | `()` |
| BVA-IN-04 | Half-infinite overlap | a=`(-inf, 4]`, b=`[2, +inf)` | `[2, 4]` |
| BVA-IN-05 | Disjoint with epsilon separation | a=`[1, 2]`, b=`[2.0001, 4]` | `()` |

---

### 2.2 Method `Interval.union(other)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-UN-01 | Overlapping intervals | Valid | a=`[1, 5]`, b=`[3, 8]` | `[1, 8]` |
| ECP-UN-02 | Disjoint intervals | Valid | a=`[1, 3]`, b=`[6, 9]` | `[1, 3] \| [6, 9]` |
| ECP-UN-03 | Subset interval | Valid | a=`[1, 10]`, b=`[3, 6]` | `[1, 10]` |
| ECP-UN-04 | Union with empty | Valid | a=`[2, 6]`, b=`()` | `[2, 6]` |
| ECP-UN-05 | Union with self | Valid | a=`[2, 6]`, b=`[2, 6]` | `[2, 6]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-UN-01 | Adjacent closed and open (merges) | a=`[1, 3)`, b=`[3, 5]` | `[1, 5]` |
| BVA-UN-02 | Adjacent open and closed (merges) | a=`[1, 3]`, b=`(3, 5]` | `[1, 5]` |
| BVA-UN-03 | Adjacent open and open (does not merge) | a=`[1, 3)`, b=`(3, 5]` | `[1, 3) \| (3, 5]` |
| BVA-UN-04 | Touching closed endpoints (merges) | a=`[1, 4]`, b=`[4, 7]` | `[1, 7]` |
| BVA-UN-05 | Complementary half-infinite intervals | a=`(-inf, 0]`, b=`[0, +inf)` | `(-inf, +inf)` |

---

## 3. Module `idict`

### 3.1 Method `IntervalDict.__setitem__(key, value)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Operations | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-DS-01 | Set single value key | Valid | `d[2] = "v"` | `d[2] == "v"`, domain `[2, 2]` |
| ECP-DS-02 | Set atomic interval key | Valid | `d[[1, 5]] = "v"` | `d[[1, 5]]` is sub-dict, value `"v"` |
| ECP-DS-03 | Overwrite with same value | Valid | `d[[1, 3]] = "v"`, then `d[[3, 6]] = "v"` | Merged domain `[1, 6]` mapped to `"v"` |
| ECP-DS-04 | Overwrite with different value | Valid | `d[[1, 5]] = "a"`, then `d[[2, 4]] = "b"` | Splits: `[1, 2) -> "a"`, `[2, 4] -> "b"`, `(4, 5] -> "a"` |
| ECP-DS-05 | Set with empty interval | Valid | `d[empty()] = "v"` | Domain remains empty |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Operations | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-DS-01 | Set exact endpoint overwrite | `d[[1, 5]] = "a"`, `d[5] = "b"` | `[1, 5) -> "a"`, `[5, 5] -> "b"` |
| BVA-DS-02 | Set adjacent interval same value | `d[[1, 3)] = "a"`, `d[[3, 5]] = "a"` | Merges to `[1, 5] -> "a"` |
| BVA-DS-03 | Complete domain overwrite | `d[[1, 5]] = "a"`, `d[[0, 6]] = "b"` | Entire `[0, 6]` replaced by `"b"` |
| BVA-DS-04 | Set sub-interval at lower boundary | `d[[1, 5]] = "a"`, `d[[1, 2]] = "b"` | `[1, 2] -> "b"`, `(2, 5] -> "a"` |
| BVA-DS-05 | Set sub-interval at upper boundary | `d[[1, 5]] = "a"`, `d[[4, 5]] = "b"` | `[1, 4) -> "a"`, `[4, 5] -> "b"` |

---

### 3.2 Method `IntervalDict.__getitem__(key)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Setup & Lookup Key | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-DG-01 | Single point inside stored interval | Valid | `d[[1, 5]] = "v"`; `d[3]` | Returns `"v"` |
| ECP-DG-02 | Single point outside stored domain | Valid (Error) | `d[[1, 5]] = "v"`; `d[10]` | Raises `KeyError(10)` |
| ECP-DG-03 | Sub-interval query | Valid | `d[[1, 5]] = "v"`; `d[[2, 4]]` | IntervalDict with `[2, 4]: "v"` |
| ECP-DG-04 | Disjoint interval query | Valid | `d[[1, 5]] = "v"`; `d[[8, 10]]` | Empty IntervalDict |
| ECP-DG-05 | Empty interval query | Valid | `d[[1, 5]] = "v"`; `d[empty()]` | Empty IntervalDict |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Setup & Lookup Key | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-DG-01 | Query exact closed lower bound | `d[[1, 5]] = "v"`; `d[1]` | Returns `"v"` |
| BVA-DG-02 | Query exact open lower bound | `d[(1, 5]] = "v"`; `d[1]` | Raises `KeyError(1)` |
| BVA-DG-03 | Query exact closed upper bound | `d[[1, 5]] = "v"`; `d[5]` | Returns `"v"` |
| BVA-DG-04 | Query exact open upper bound | `d[[1, 5)] = "v"`; `d[5]` | Raises `KeyError(5)` |
| BVA-DG-05 | Query point just outside closed bound | `d[[1, 5]] = "v"`; `d[5.0001]` | Raises `KeyError(5.0001)` |
