# portion-unit-testing

Repository for unit testing the portion library.

## Group members

- Muhammad Arslan, Roll No. 24F-3059 (Member A)
- Muhammad Talha, Roll No. 24F-3085 (Member B)

## Project Information

- Project Name: portion
- Repository: https://github.com/AlexandreDecan/portion
- Licence: LGPL-3.0-or-later
- Python Version: 3.14.6

## Setup

### Windows PowerShell

Run the automated setup script:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup.ps1
```

Or execute manually:

```powershell
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -e project
pip install -r requirements-dev.txt
pytest project
```

### Linux and macOS

Run the automated setup script:

```bash
bash scripts/setup.sh
```

Or execute manually:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e project
pip install -r requirements-dev.txt
pytest project
```

## How to run

### 1. Run Everything

```bash
pytest
```

### 2. Run One Suite (Folder)

```bash
pytest tests_custom/interval/
pytest tests_custom/ops/
pytest tests_custom/idict/
```

### 3. Run One Group (-m)

```bash
pytest -m smoke
pytest -m bva
pytest -m ecp
pytest -m csv
pytest -m regression
```

### 4. Run in Parallel (-n 2)

```bash
pytest -n 2
```

### 5. Run in a Fixed Order

The `pytest_collection_modifyitems` hook in `conftest.py` automatically sorts tests by group marker in the order `smoke`, `ecp`, `bva`, `csv`, `regression`. To run tests sequentially in this order:

```bash
pytest -o addopts="" -v
```

### 6. Generate HTML Report and Coverage

```bash
pytest --cov=portion --html=reports/report.html --self-contained-html
```

## Deliverables

### Documentation & Reports
- `docs/test_design_arslan.md` - ECP and BVA test design for Member A functions
- `docs/test_design_talha.md` - ECP and BVA test design for Member B functions
- `docs/setup_talha.md` - Environment setup validation and confirmation for Member B
- `docs/running_talha.md` - Test execution guide and suite descriptions for Member B
- `docs/summary_report_arslan.md` - Summary report for Member A (Muhammad Arslan)
- `docs/summary_report_talha.md` - Summary report for Member B (Muhammad Talha)
- `docs/summary_report.md` - Comprehensive project summary report for the whole group

### Excel Spreadsheets
- `docs/test_cases_arslan.xlsx` - Excel test cases with actual execution results for Member A
- `docs/test_cases_talha.xlsx` - Excel test cases with actual execution results for Member B

### Test Data (CSV)
- `data/arslan_data.csv` - Data-driven test inputs for interval intersection
- `data/talha_data.csv` - Data-driven test inputs for scalar containment

### Setup Video
- `docs/setup_video.mp4` - Video demonstration of environment setup and test suite execution

### Automation Scripts
- `scripts/setup.ps1` - Automated setup script for Windows PowerShell
- `scripts/setup.sh` - Automated setup script for Linux/macOS
- `scripts/run_suites_talha.ps1` - Automated test suite runner for Windows PowerShell
- `scripts/run_suites_talha.sh` - Automated test suite runner for Linux/macOS

### Configuration & Root Files
- `pytest.ini` - Pytest configuration and marker declarations
- `conftest.py` - Pytest collection hook sorting tests by marker order
- `requirements-dev.txt` - Pinned development dependencies
- `.gitignore` - Git ignore rules excluding virtual environments and reports
- `README.md` - Project documentation, setup guide, execution instructions, and deliverables
