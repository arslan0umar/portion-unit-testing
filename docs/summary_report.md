# Final Project Summary Report - portion Unit Testing

## Project Overview

- Project Name: portion
- Repository: https://github.com/AlexandreDecan/portion
- Licence: LGPL-3.0-or-later (GNU Lesser General Public License v3.0 or later)
- Description: Python interval arithmetic and data structure library.

---

## Group Members

| Name | Roll Number | Role |
| :--- | :--- | :--- |
| Muhammad Arslan | 24F-3059 | Member A |
| Muhammad Talha | 24F-3085 | Member B |

---

## Environment and Test Engine

- Python Version: `3.14.6`
- Pytest Version: `9.1.1`
- Plugins: `pytest-xdist (3.8.0)`, `pytest-cov (7.1.0)`, `pytest-html (4.2.0)`, `pytest-order (1.5.0)`, `pytest-benchmark (5.3.0)`

---

## Test Execution Summary

Real execution results across the complete custom test suite:

- Total Tests Collected: **390**
- Total Tests Passed: **390**
- Total Tests Failed: **0**
- Total Tests Skipped: **0**
- Execution Status: **100% Green**

### Test Breakdown by Member and Marker

| Marker Group | Member A (Arslan) | Member B (Talha) | Combined Total |
| :--- | :--- | :--- | :--- |
| `smoke` | 11 | 15 | 26 |
| `ecp` | 55 | 85 | 140 |
| `bva` | 54 | 75 | 129 |
| `csv` | 24 | 32 | 56 |
| `regression` | 12 | 27 | 39 |
| **Total** | **156** | **234** | **390** |

---

## Code Coverage Results

Coverage measured across the `portion` package (`--cov=portion`):

| Module | Statements | Missed | Coverage |
| :--- | :--- | :--- | :--- |
| `portion/__init__.py` | 11 | 0 | 100% |
| `portion/api.py` | 20 | 9 | 55% |
| `portion/const.py` | 53 | 5 | 91% |
| `portion/dict.py` | 211 | 101 | 52% |
| `portion/func.py` | 40 | 23 | 42% |
| `portion/interval.py` | 338 | 83 | 75% |
| `portion/io.py` | 81 | 25 | 69% |
| **Total** | **754** | **246** | **67%** |

HTML coverage report generated at `reports/cov/index.html`.

---

## Testing Techniques & Methodologies

1. **Equivalence Class Partitioning (ECP)**: Partitioned domain inputs into valid and invalid classes for intervals, operations, and dictionaries.
2. **Boundary Value Analysis (BVA)**: Targeted edge cases including empty sets, singletons, infinities (`-inf`, `+inf`), adjacent intervals, and boundary openness.
3. **Data-Driven Testing (CSV)**: Parameterized test execution via external CSV files (`data/arslan_data.csv`, `data/talha_data.csv`) using the Python `csv` module.
4. **Pytest Parametrization**: Used `@pytest.mark.parametrize` across all major test functions for concise and extensive input coverage.
5. **Fixed Ordering**: Used `@pytest.mark.order(n)` to enforce deterministic test sequence within each test file.
6. **Hook-Based Sorting**: Implemented `pytest_collection_modifyitems` hook in `conftest.py` sorting test execution across marker groups: `smoke` -> `ecp` -> `bva` -> `csv` -> `regression`.
7. **Parallel Test Execution**: Utilized `pytest-xdist` (`-n 2 --dist loadfile`) for multi-worker parallel execution.
8. **Custom Markers**: Applied custom markers (`smoke`, `ecp`, `bva`, `csv`, `regression`) declared in `pytest.ini`.

---

## Deliverables & File Paths

### Test Suites
- `tests_custom/interval/test_interval_arslan.py`
- `tests_custom/interval/test_interval_talha.py`
- `tests_custom/ops/test_ops_arslan.py`
- `tests_custom/ops/test_ops_csv_arslan.py`
- `tests_custom/ops/test_ops_talha.py`
- `tests_custom/ops/test_contains_csv_talha.py`
- `tests_custom/idict/test_idict_arslan.py`
- `tests_custom/idict/test_idict_talha.py`

### Test Data (CSV)
- `data/arslan_data.csv`
- `data/talha_data.csv`

### Test Cases Spreadsheets (Excel)
- `docs/test_cases_arslan.xlsx`
- `docs/test_cases_talha.xlsx`

### Test Design Documents
- `docs/test_design_arslan.md`
- `docs/test_design_talha.md`

### Summary & Setup Reports
- `docs/summary_report_arslan.md`
- `docs/summary_report_talha.md`
- `docs/summary_report.md`
- `docs/setup_talha.md`
- `docs/running_talha.md`

### Setup Video
- `docs/setup_video.mp4`

### Scripts
- `scripts/setup.ps1`
- `scripts/setup.sh`
- `scripts/run_suites_talha.ps1`
- `scripts/run_suites_talha.sh`

### Project Configuration
- `pytest.ini`
- `conftest.py`
- `requirements-dev.txt`
- `.gitignore`
- `README.md`
- `project/` (source code of portion)

---

## Git Commit Contributions

From `git log` analysis:

| Member | Git Author Names | Commit Count |
| :--- | :--- | :--- |
| Muhammad Arslan (24F-3059) | `arslan0umar`, `Muhammad Arslan` | 9 commits |
| Muhammad Talha (24F-3085) | `mtalha055` | 6 commits |
| **Total Prior Commits** | | **15 commits** |
