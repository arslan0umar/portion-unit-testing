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
