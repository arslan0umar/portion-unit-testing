$dir = Split-Path -Parent $PSScriptRoot
if (-not $dir) {
    $dir = Get-Location
}
Set-Location $dir
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    . .\.venv\Scripts\Activate.ps1
}

pytest tests_custom/interval
pytest tests_custom/ops
pytest tests_custom/idict

pytest -m smoke
pytest -m ecp
pytest -m bva
pytest -m csv
pytest -m regression

pytest -n 2
