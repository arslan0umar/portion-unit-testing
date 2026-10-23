# Test Execution Guide - Member B (Talha)

This guide documents the test suite structure, execution orders, and automated runner scripts.

## Automated Test Runner Scripts

Two runner scripts automate complete test execution across suites and marker groups in fixed order, concluding with a parallel execution:

- Windows PowerShell: `scripts/run_suites_talha.ps1`
- Bash (Linux / macOS): `scripts/run_suites_talha.sh`

### How to Run

#### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_suites_talha.ps1
```

#### Bash

```bash
bash scripts/run_suites_talha.sh
```

---

## Execution Sequence

The scripts execute tests in the following defined stages:

### Stage 1: Suite Execution in Fixed Order

1. **Interval Suite**: `pytest tests_custom/interval`
   Tests foundational interval representation, bound types, and properties (`lower`, `upper`, `left`, `right`, `atomic`, `empty`).
2. **Operations Suite**: `pytest tests_custom/ops`
   Tests interval operations including `complement`, `difference`, `overlaps`, `adjacent`, and `__contains__`.
3. **IntervalDict Suite**: `pytest tests_custom/idict`
   Tests mapping operations including `IntervalDict.get`, `IntervalDict.domain`, `to_string`, and `from_string`.

### Stage 2: Group Execution by Marker in Fixed Order

1. **Smoke**: `pytest -m smoke`
   Quick health verification for fundamental operations.
2. **ECP (Equivalence Class Partitioning)**: `pytest -m ecp`
   Verifies standard partitions across input conditions.
3. **BVA (Boundary Value Analysis)**: `pytest -m bva`
   Verifies edge boundaries, infinite bounds, and empty states.
4. **CSV (Data Driven Tests)**: `pytest -m csv`
   Executes CSV-driven test cases from `data/talha_data.csv`.
5. **Regression**: `pytest -m regression`
   Verifies edge interactions, mathematical identities, and idempotence.

### Stage 3: Full Parallel Execution

- **Parallel Run**: `pytest -n 2`
  Executes all collected tests across two worker processes using `pytest-xdist`.
