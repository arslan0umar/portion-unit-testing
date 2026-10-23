# Environment Setup Confirmation - Member B (Talha)

This document confirms that the development and testing environment setup has been successfully executed and validated on this machine.

## System & Environment Details

- Operating System: Windows 11 / Windows amd64
- Shell: PowerShell
- Git Identity: `mtalha055` (`f243085@cfd.nu.edu.pk`)
- Python Version: `3.14.6`
- Virtual Environment: `.venv` (created via `scripts/setup.ps1`)
- Package Under Test: `portion` (version `2.7.0rc1`, installed in editable mode from `project/`)

## Verification Steps & Commands

### 1. Automated Setup Script Execution

The automated setup script `scripts/setup.ps1` was executed:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup.ps1
```

The script performed the following actions:
- Initialized a Python virtual environment at `.venv`
- Activated the virtual environment
- Installed the project in editable mode (`pip install -e project`)
- Installed development dependencies (`pip install -r requirements-dev.txt`)
- Ran initial test suite on `project/`

### 2. Tool Version Verification

```powershell
.\.venv\Scripts\python.exe --version
# Output: Python 3.14.6

.\.venv\Scripts\pytest.exe --version
# Output: pytest 9.1.1
```

### 3. Pytest Execution Results

Execution of `pytest project`:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\dell\Documents\sqe_talha\project
configfile: pyproject.toml
plugins: benchmark-5.3.0, cov-7.1.0, html-4.2.0, metadata-3.1.1, order-1.5.0, xdist-3.8.0
collected 241 items

project\tests\test_const.py ........                                     [  3%]
project\tests\test_dict.py ............................................. [ 21%]
...........sss                                                           [ 27%]
project\tests\test_discrete.py .........                                 [ 31%]
project\tests\test_doc.py .                                              [ 31%]
project\tests\test_func.py ........                                      [ 35%]
project\tests\test_interval.py ......................................... [ 52%]
ssss.........................ssss....................................... [ 82%]
.                                                                        [ 82%]
project\tests\test_io.py ..........................................      [100%]

======================= 230 passed, 11 skipped in 1.62s =======================
Exit code: 0
```

Initial execution of custom tests in `tests_custom`:

```powershell
.\.venv\Scripts\pytest.exe
```

Output confirmed 156 existing test cases passed with exit code 0.
Setup is fully operational and green.
