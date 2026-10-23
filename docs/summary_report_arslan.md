# Summary Report - Member A (Muhammad Arslan)

## Member Details

- Name: Muhammad Arslan
- Roll No.: 24F-3059
- Role: Member A

---

## 1. Owned Files

### Test Files
- `tests_custom/interval/test_interval_arslan.py`
- `tests_custom/ops/test_ops_arslan.py`
- `tests_custom/ops/test_ops_csv_arslan.py`
- `tests_custom/idict/test_idict_arslan.py`

### Data and Documentation Files
- `data/arslan_data.csv`
- `docs/test_cases_arslan.xlsx`
- `docs/test_design_arslan.md`
- `docs/summary_report_arslan.md`

### Shared Project Files
- `pytest.ini`
- `conftest.py`
- `scripts/setup.ps1`
- `scripts/setup.sh`
- `README.md`

---

## 2. Functions Tested

### Module `interval`
- `closed(lower, upper)`: Closed interval creation, singleton handling, inverted bounds, infinite endpoints.
- `open(lower, upper)`: Open interval creation, empty interval handling, unbounded intervals.
- `openclosed(lower, upper)`: Left-open, right-closed interval creation.
- `closedopen(lower, upper)`: Left-closed, right-open interval creation.
- `singleton(value)`: Point intervals for integer, float, string, and infinite values.
- `empty()`: Empty interval creation, empty and atomic property validations.
- `Interval.replace(...)`: Updating lower, upper, and openness bounds with values and callables.

### Module `ops`
- `Interval.intersection(other)`: Disjoint, overlapping, subset, non-atomic disjunctions, and edge boundaries.
- `Interval.union(other)`: Merging adjacent intervals, disjoint intervals, subset unions, and operator equivalence.

### Module `idict`
- `IntervalDict.__setitem__(key, value)`: Setting single values, atomic intervals, overwriting keys, splitting intervals, and setting empty keys.
- `IntervalDict.__getitem__(key)`: Retrieving values by single key, querying sub-intervals, handling disjoint queries, and KeyError handling.

---

## 3. Test Counts by Marker (Real Execution)

All 156 tests collected from Member A test files pass green:

| Marker | Test Count | Status |
| :--- | :--- | :--- |
| `smoke` | 11 | Passed |
| `ecp` | 55 | Passed |
| `bva` | 54 | Passed |
| `csv` | 24 | Passed |
| `regression` | 12 | Passed |
| **Total** | **156** | **All Passed** |

---

## 4. Data-Driven and Excel Artifacts

- `data/arslan_data.csv`: Contains 6 test cases for interval intersection covering normal overlap, disjoint, boundary touching, subset containment, negative spans, and half-infinite intervals.
- `docs/test_cases_arslan.xlsx`: Contains 17 documented test cases across `interval`, `ops`, and `idict` modules with columns `TC ID`, `Module`, `Function`, `Technique`, `Input`, `Expected`, `Actual`, and `Status` (`PASS`).
- `docs/test_design_arslan.md`: Exhaustive ECP and BVA design specifications with input conditions, boundaries, and expected results.
