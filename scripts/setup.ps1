$dir = Split-Path -Parent $PSScriptRoot
if (-not $dir) {
    $dir = Get-Location
}
Set-Location $dir
if (Get-Command py -ErrorAction SilentlyContinue) {
    py -m venv .venv
} else {
    python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1
pip install -e project
pip install -r requirements-dev.txt
pytest project
$res = $LASTEXITCODE
Write-Output "Exit code: $res"
exit $res
