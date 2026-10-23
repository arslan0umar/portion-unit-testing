# portion-unit-testing

Repository for unit testing the portion library.

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
