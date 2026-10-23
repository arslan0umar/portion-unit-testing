# Test Design Document - Member B (Talha)

This document contains Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA) test designs for the assigned functions and properties in `portion`.

---

## 1. Module `interval`

### 1.1 Property `lower`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-LW-01 | Standard closed interval | Valid (finite positive) | `[1, 5]` | `1` |
| ECP-LW-02 | Standard open interval | Valid (negative bounds) | `(-10, -2)` | `-10` |
| ECP-LW-03 | Half-unbounded lower | Valid (-inf bound) | `(-inf, 5]` | `-inf` |
| ECP-LW-04 | Degenerate singleton | Valid (point value) | `[42]` | `42` |
| ECP-LW-05 | Disjunction of intervals | Valid (multi-part) | `[1, 2] \| [4, 5]` | `1` |
| ECP-LW-06 | Empty interval | Valid (empty default) | `()` | `+inf` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-LW-01 | Empty interval boundary | `()` | `+inf` |
| BVA-LW-02 | Singleton at zero | `[0]` | `0` |
| BVA-LW-03 | Float boundary value | `[0.0001, 2.5]` | `0.0001` |
| BVA-LW-04 | Negative infinity bound | `(-inf, 0)` | `-inf` |
| BVA-LW-05 | Adjacent disjunction lower bound | `[0, 1) \| [2, 3)` | `0` |

---

### 1.2 Property `upper`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-UP-01 | Standard closed interval | Valid (finite positive) | `[1, 5]` | `5` |
| ECP-UP-02 | Standard open interval | Valid (negative bounds) | `(-10, -2)` | `-2` |
| ECP-UP-03 | Half-unbounded upper | Valid (+inf bound) | `[0, +inf)` | `+inf` |
| ECP-UP-04 | Degenerate singleton | Valid (point value) | `[42]` | `42` |
| ECP-UP-05 | Disjunction of intervals | Valid (multi-part) | `[1, 2] \| [4, 8]` | `8` |
| ECP-UP-06 | Empty interval | Valid (empty default) | `()` | `-inf` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-UP-01 | Empty interval boundary | `()` | `-inf` |
| BVA-UP-02 | Singleton at zero | `[0]` | `0` |
| BVA-UP-03 | Float precision upper bound | `[0, 1.0001]` | `1.0001` |
| BVA-UP-04 | Positive infinity bound | `(-10, +inf)` | `+inf` |
| BVA-UP-05 | Multi-interval highest upper bound | `[-5, -1] \| [0, 9]` | `9` |

---

### 1.3 Property `left`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-LF-01 | Closed left boundary | Valid (closed) | `[1, 5]` | `Bound.CLOSED` |
| ECP-LF-02 | Open left boundary | Valid (open) | `(1, 5]` | `Bound.OPEN` |
| ECP-LF-03 | Degenerate singleton | Valid (closed) | `[7]` | `Bound.CLOSED` |
| ECP-LF-04 | Disjunction starting with closed | Valid (closed) | `[1, 2] \| (4, 5)` | `Bound.CLOSED` |
| ECP-LF-05 | Disjunction starting with open | Valid (open) | `(1, 2) \| [4, 5]` | `Bound.OPEN` |
| ECP-LF-06 | Empty interval | Valid (open default) | `()` | `Bound.OPEN` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-LF-01 | Empty interval default left bound | `()` | `Bound.OPEN` |
| BVA-LF-02 | Unbounded negative infinity left side | `(-inf, 2]` | `Bound.OPEN` |
| BVA-LF-03 | Minimal singleton left bound | `[0]` | `Bound.CLOSED` |
| BVA-LF-04 | Open left with zero boundary | `(0, 1]` | `Bound.OPEN` |
| BVA-LF-05 | Closed left with float boundary | `[1.5, 3.5]` | `Bound.CLOSED` |

---

### 1.4 Property `right`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-RT-01 | Closed right boundary | Valid (closed) | `[1, 5]` | `Bound.CLOSED` |
| ECP-RT-02 | Open right boundary | Valid (open) | `[1, 5)` | `Bound.OPEN` |
| ECP-RT-03 | Degenerate singleton | Valid (closed) | `[9]` | `Bound.CLOSED` |
| ECP-RT-04 | Disjunction ending with closed | Valid (closed) | `(1, 2) \| [4, 6]` | `Bound.CLOSED` |
| ECP-RT-05 | Disjunction ending with open | Valid (open) | `[1, 2] \| [4, 6)` | `Bound.OPEN` |
| ECP-RT-06 | Empty interval | Valid (open default) | `()` | `Bound.OPEN` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-RT-01 | Empty interval default right bound | `()` | `Bound.OPEN` |
| BVA-RT-02 | Unbounded positive infinity right side | `[-1, +inf)` | `Bound.OPEN` |
| BVA-RT-03 | Singleton right bound | `[0]` | `Bound.CLOSED` |
| BVA-RT-04 | Open right with zero boundary | `[-1, 0)` | `Bound.OPEN` |
| BVA-RT-05 | Closed right with float boundary | `[0.1, 0.9]` | `Bound.CLOSED` |

---

### 1.5 Property `atomic`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-AT-01 | Empty interval | Valid (atomic) | `()` | `True` |
| ECP-AT-02 | Single closed interval | Valid (atomic) | `[1, 5]` | `True` |
| ECP-AT-03 | Single open interval | Valid (atomic) | `(2, 8)` | `True` |
| ECP-AT-04 | Singleton point interval | Valid (atomic) | `[3]` | `True` |
| ECP-AT-05 | Fully unbounded interval | Valid (atomic) | `(-inf, +inf)` | `True` |
| ECP-AT-06 | Disjunction with gap | Valid (non-atomic) | `[1, 2] \| [4, 5]` | `False` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-AT-01 | Empty interval boundary | `()` | `True` |
| BVA-AT-02 | Two intervals sharing open boundary (gap of 1 point) | `(1, 2) \| (2, 3)` | `False` |
| BVA-AT-03 | Two intervals touching closed-open (merges to 1) | `[1, 2] \| (2, 3]` | `True` |
| BVA-AT-04 | Three disjoint components | `[1, 2] \| [4, 5] \| [7, 8]` | `False` |
| BVA-AT-05 | Overlapping disjunction merging to atomic | `[1, 4] \| [3, 6]` | `True` |

---

### 1.6 Property `empty`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-EM-01 | Explicit empty constructor | Valid (empty) | `empty()` | `True` |
| ECP-EM-02 | Inverted bound construction | Valid (empty) | `closed(5, 1)` | `True` |
| ECP-EM-03 | Open interval with equal bounds | Valid (empty) | `open(3, 3)` | `True` |
| ECP-EM-04 | Half-open with equal bounds | Valid (empty) | `closedopen(2, 2)` | `True` |
| ECP-EM-05 | Standard closed interval | Valid (non-empty) | `[1, 5]` | `False` |
| ECP-EM-06 | Singleton interval | Valid (non-empty) | `[0]` | `False` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-EM-01 | Open equal bounds boundary | `open(4, 4)` | `True` |
| BVA-EM-02 | Closed equal bounds boundary | `closed(4, 4)` | `False` |
| BVA-EM-03 | Disjoint intersection resulting in empty | `[1, 2] & [3, 4]` | `True` |
| BVA-EM-04 | Touching open intersection resulting in empty | `[1, 3) & [3, 5]` | `True` |
| BVA-EM-05 | Minimal non-empty float span | `[1.0, 1.00001]` | `False` |

---

## 2. Module `ops`

### 2.1 Method `Interval.complement()` / `~`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-CP-01 | Empty interval | Valid | `()` | `(-inf, +inf)` |
| ECP-CP-02 | Fully unbounded interval | Valid | `(-inf, +inf)` | `()` |
| ECP-CP-03 | Finite closed interval | Valid | `[1, 5]` | `(-inf, 1) \| (5, +inf)` |
| ECP-CP-04 | Finite open interval | Valid | `(1, 5)` | `(-inf, 1] \| [5, +inf)` |
| ECP-CP-05 | Half-unbounded interval | Valid | `[0, +inf)` | `(-inf, 0)` |
| ECP-CP-06 | Multi-component disjunction | Valid | `[1, 2] \| [4, 5]` | `(-inf, 1) \| (2, 4) \| (5, +inf)` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Target Interval | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-CP-01 | Singleton point complement | `[0]` | `(-inf, 0) \| (0, +inf)` |
| BVA-CP-02 | Left half-unbounded closed | `(-inf, 2]` | `(2, +inf)` |
| BVA-CP-03 | Left half-unbounded open | `(-inf, 2)` | `[2, +inf)` |
| BVA-CP-04 | Symmetric around zero | `[-1, 1]` | `(-inf, -1) \| (1, +inf)` |
| BVA-CP-05 | Inversion of double complement | `~~[2, 4]` | `[2, 4]` |

---

### 2.2 Method `Interval.difference(other)` / `-`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-DF-01 | Overlapping intervals | Valid | a=`[1, 5]`, b=`[3, 7]` | `[1, 3)` |
| ECP-DF-02 | Disjoint intervals | Valid | a=`[1, 3]`, b=`[5, 8]` | `[1, 3]` |
| ECP-DF-03 | Subtracting subset | Valid | a=`[1, 10]`, b=`[3, 7]` | `[1, 3) \| (7, 10]` |
| ECP-DF-04 | Subtracting superset | Valid | a=`[3, 5]`, b=`[1, 10]` | `()` |
| ECP-DF-05 | Self difference | Valid | a=`[1, 5]`, b=`[1, 5]` | `()` |
| ECP-DF-06 | Difference with empty | Valid | a=`[1, 5]`, b=`()` | `[1, 5]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-DF-01 | Touching at closed endpoint | a=`[1, 4]`, b=`[4, 8]` | `[1, 4)` |
| BVA-DF-02 | Touching at open endpoint | a=`[1, 4)`, b=`[4, 8]` | `[1, 4)` |
| BVA-DF-03 | Subtracting singleton endpoint | a=`[1, 5]`, b=`[5]` | `[1, 5)` |
| BVA-DF-04 | Empty minus non-empty | a=`()`, b=`[1, 5]` | `()` |
| BVA-DF-05 | Subtracting infinite half-line | a=`[-5, 5]`, b=`[0, +inf)` | `[-5, 0)` |

---

### 2.3 Method `Interval.overlaps(other)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-OV-01 | Partially overlapping closed | Valid (overlap) | a=`[1, 5]`, b=`[3, 7]` | `True` |
| ECP-OV-02 | Completely disjoint | Valid (no overlap) | a=`[1, 3]`, b=`[5, 8]` | `False` |
| ECP-OV-03 | Strict subset containment | Valid (overlap) | a=`[1, 10]`, b=`[3, 6]` | `True` |
| ECP-OV-04 | Empty interval tested against non-empty | Valid (no overlap) | a=`[1, 5]`, b=`()` | `False` |
| ECP-OV-05 | Both empty intervals | Valid (no overlap) | a=`()`, b=`()` | `False` |
| ECP-OV-06 | Identical intervals | Valid (overlap) | a=`[2, 6]`, b=`[2, 6]` | `True` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-OV-01 | Touching closed boundary | a=`[1, 4]`, b=`[4, 8]` | `True` |
| BVA-OV-02 | Touching open-closed boundary | a=`[1, 4)`, b=`[4, 8]` | `False` |
| BVA-OV-03 | Touching open-open boundary | a=`[1, 4)`, b=`(4, 8]` | `False` |
| BVA-OV-04 | Epsilon separation | a=`[1, 2]`, b=`[2.0001, 5]` | `False` |
| BVA-OV-05 | Infinite boundary overlap | a=`(-inf, 0]`, b=`[0, +inf)` | `True` |

---

### 2.4 Method `Interval.adjacent(other)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-AD-01 | Closed-open touching | Valid (adjacent) | a=`[1, 3]`, b=`(3, 5]` | `True` |
| ECP-AD-02 | Open-closed touching | Valid (adjacent) | a=`[1, 3)`, b=`[3, 5]` | `True` |
| ECP-AD-03 | Disjoint with non-zero gap | Valid (not adjacent) | a=`[1, 2]`, b=`[4, 5]` | `False` |
| ECP-AD-04 | Overlapping intervals | Valid (not adjacent) | a=`[1, 4]`, b=`[3, 6]` | `False` |
| ECP-AD-05 | Empty with atomic interval | Valid (adjacent) | a=`()`, b=`[1, 5]` | `True` |
| ECP-AD-06 | Two empty intervals | Valid (adjacent) | a=`()`, b=`()` | `True` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Inputs a and b | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-AD-01 | Touching closed-closed (overlaps, non-empty intersection) | a=`[1, 3]`, b=`[3, 5]` | `False` |
| BVA-AD-02 | Touching open-open (gap of 1 element, non-atomic union) | a=`[1, 3)`, b=`(3, 5]` | `False` |
| BVA-AD-03 | Infinite adjacent boundary | a=`(-inf, 0]`, b=`(0, +inf)` | `True` |
| BVA-AD-04 | Float adjacent boundary | a=`[0.0, 1.5)`, b=`[1.5, 3.0]` | `True` |
| BVA-AD-05 | Adjacent empty with non-atomic interval | a=`()`, b=`[1, 2] \| [4, 5]` | `False` |

---

### 2.5 Operator `item in Interval` / `__contains__`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Container & Item | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-CN-01 | Point strictly inside closed interval | Valid | `3 in [1, 5]` | `True` |
| ECP-CN-02 | Point strictly outside interval | Valid | `8 in [1, 5]` | `False` |
| ECP-CN-03 | Sub-interval strictly inside | Valid | `[2, 4] in [1, 5]` | `True` |
| ECP-CN-04 | Sub-interval partially overlapping | Valid | `[3, 7] in [1, 5]` | `False` |
| ECP-CN-05 | Empty interval containment | Valid | `() in [1, 5]` | `True` |
| ECP-CN-06 | Point inside multi-component interval | Valid | `4 in [1, 2] \| [4, 6]` | `True` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Container & Item | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-CN-01 | Point on closed lower bound | `1 in [1, 5]` | `True` |
| BVA-CN-02 | Point on open lower bound | `1 in (1, 5]` | `False` |
| BVA-CN-03 | Point on closed upper bound | `5 in [1, 5]` | `True` |
| BVA-CN-04 | Point on open upper bound | `5 in [1, 5)` | `False` |
| BVA-CN-05 | Point just outside bound | `5.0001 in [1, 5]` | `False` |

---

## 3. Module `idict`

### 3.1 Method `IntervalDict.get(key, default=None)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Setup & Call | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-GT-01 | Point key present | Valid | `d[[1, 5]] = "v"`; `d.get(3)` | `"v"` |
| ECP-GT-02 | Point key missing without default | Valid | `d[[1, 5]] = "v"`; `d.get(10)` | `None` |
| ECP-GT-03 | Point key missing with custom default | Valid | `d[[1, 5]] = "v"`; `d.get(10, "missing")` | `"missing"` |
| ECP-GT-04 | Interval key completely covered | Valid | `d[[1, 5]] = "v"`; `d.get([2, 4])` | `{[2, 4]: "v"}` |
| ECP-GT-05 | Interval key partially covered | Valid | `d[[1, 5]] = "v"`; `d.get([0, 2], "x")` | `{[0, 1): "x", [1, 2]: "v"}` |
| ECP-GT-06 | Empty interval key | Valid | `d[[1, 5]] = "v"`; `d.get(empty())` | `{}` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Setup & Call | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-GT-01 | Point query on closed lower boundary | `d[[1, 5]] = "v"`; `d.get(1)` | `"v"` |
| BVA-GT-02 | Point query on open lower boundary | `d[(1, 5]] = "v"`; `d.get(1, "def")` | `"def"` |
| BVA-GT-03 | Point query on closed upper boundary | `d[[1, 5]] = "v"`; `d.get(5)` | `"v"` |
| BVA-GT-04 | Point query on open upper boundary | `d[[1, 5)] = "v"`; `d.get(5, "def")` | `"def"` |
| BVA-GT-05 | Point query on completely empty dict | `d = IntervalDict()`; `d.get(0, "empty")` | `"empty"` |

---

### 3.2 Method `IntervalDict.domain()`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Setup & Call | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-DM-01 | Empty IntervalDict | Valid | `d = IntervalDict()`; `d.domain()` | `()` |
| ECP-DM-02 | Single closed interval key | Valid | `d[[1, 5]] = "a"`; `d.domain()` | `[1, 5]` |
| ECP-DM-03 | Multiple disjoint keys | Valid | `d[[1, 2]] = "a"`, `d[[4, 6]] = "b"`; `d.domain()` | `[1, 2] \| [4, 6]` |
| ECP-DM-04 | Merged adjacent keys with same value | Valid | `d[[1, 3)] = "a"`, `d[[3, 5]] = "a"`; `d.domain()` | `[1, 5]` |
| ECP-DM-05 | Contiguous keys with different values | Valid | `d[[1, 3)] = "a"`, `d[[3, 5]] = "b"`; `d.domain()` | `[1, 5]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Setup & Call | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-DM-01 | Empty dict domain emptiness | `d = IntervalDict()`; `d.domain().empty` | `True` |
| BVA-DM-02 | Singleton key domain | `d[3] = "v"`; `d.domain()` | `[3]` |
| BVA-DM-03 | Half-unbounded key domain | `d[(-inf, 0]] = "v"`; `d.domain()` | `(-inf, 0]` |
| BVA-DM-04 | Domain after deleting only key | `d[[1, 5]] = "v"`; `del d[[1, 5]]`; `d.domain()` | `()` |
| BVA-DM-05 | Partial deletion shrinks domain | `d[[1, 5]] = "v"`; `del d[[1, 2]]`; `d.domain()` | `(2, 5]` |

---

### 3.3 Function `to_string(interval, conv=repr, ...)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input Interval | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-TS-01 | Empty interval | Valid | `empty()` | `"()"` |
| ECP-TS-02 | Standard closed interval | Valid | `[1, 5]` | `"[1,5]"` |
| ECP-TS-03 | Standard open interval | Valid | `(1, 5)` | `"(1,5)"` |
| ECP-TS-04 | Half-open interval | Valid | `[1, 5)` | `"[1,5)"` |
| ECP-TS-05 | Half-unbounded interval | Valid | `(-inf, 0]` | `"(-inf,0]"` |
| ECP-TS-06 | Multi-component disjunction | Valid | `[1, 2] \| [4, 5]` | `"[1,2] \| [4,5]"` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input Interval & Options | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-TS-01 | Degenerate singleton representation | `[3]` | `"[3]"` |
| BVA-TS-02 | Fully unbounded interval | `(-inf, +inf)` | `"(-inf,+inf)"` |
| BVA-TS-03 | Custom string converter | `[1, 5]` with `conv=lambda x: f"x{x}"` | `"[x1,x5]"` |
| BVA-TS-04 | Custom disjunction separator | `[1, 2] \| [4, 5]` with `disj=" OR "` | `"[1,2] OR [4,5]"` |
| BVA-TS-05 | Float bounds formatting | `[1.5, 3.5]` | `"[1.5,3.5]"` |

---

### 3.4 Function `from_string(string, conv, ...)`

#### Equivalence Class Partitioning (ECP)

| Class ID | Input Condition | Category | Input String & Converter | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| ECP-FS-01 | Closed interval string | Valid | `"[1,5]"`, `int` | `[1, 5]` |
| ECP-FS-02 | Open interval string | Valid | `"(1,5)"`, `int` | `(1, 5)` |
| ECP-FS-03 | Half-open interval string | Valid | `"[1,5)"`, `int` | `[1, 5)` |
| ECP-FS-04 | Singleton string | Valid | `"[3]"`, `int` | `[3]` |
| ECP-FS-05 | Empty interval string | Valid | `"()"`, `int` | `()` |
| ECP-FS-06 | Disjunction string | Valid | `"[1,2] \| [4,5]"`, `int` | `[1, 2] \| [4, 5]` |

#### Boundary Value Analysis (BVA)

| BVA ID | Boundary Description | Input String & Converter | Expected Result |
| :--- | :--- | :--- | :--- |
| BVA-FS-01 | Unbounded negative infinity string | `"(-inf,0]"`, `int` | `(-inf, 0]` |
| BVA-FS-02 | Unbounded positive infinity string | `"[0,+inf)"`, `int` | `[0, +inf)` |
| BVA-FS-03 | Fully unbounded string | `"(-inf,+inf)"`, `int` | `(-inf, +inf)` |
| BVA-FS-04 | Invalid syntax error handling | `"invalid"`, `int` | Raises `ValueError` |
| BVA-FS-05 | Float converter parsing | `"[1.5,4.5]"`, `float` | `[1.5, 4.5]` |
