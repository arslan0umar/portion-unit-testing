dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"
if [ ! -d ".venv" ]; then
    if command -v python3 >/dev/null 2>&1; then
        python3 -m venv .venv
    else
        python -m venv .venv
    fi
fi
if [ -f ".venv/bin/activate" ]; then
    . .venv/bin/activate
elif [ -f ".venv/Scripts/activate" ]; then
    . .venv/Scripts/activate
fi
pip install -e project
pip install -r requirements-dev.txt
pytest project
res=$?
echo "Exit code: $res"
exit $res
