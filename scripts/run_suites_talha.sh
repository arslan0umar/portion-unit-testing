dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$dir"
if [ -f ".venv/bin/activate" ]; then
    . .venv/bin/activate
fi

pytest tests_custom/interval
pytest tests_custom/ops
pytest tests_custom/idict

pytest -m smoke
pytest -m ecp
pytest -m bva
pytest -m csv
pytest -m regression

pytest -n 2
